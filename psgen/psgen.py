#!/usr/bin/env python

import argparse
import psgen
import sys
from os import path
import glob
import yaml
from tabulate import tabulate
from ps_minifier.psminifier import minify
from jinja2 import Template
import base64

def load_options(options):
    option_dict = {}
    for option in options:
        words = option.split("=", 2)
        option_dict[words[0]] = words[1]
    
    return option_dict


def load_payloads():
    builtin_payload_path = path.join(path.dirname(__file__), 'payload')
    local_payload_path = path.join(path.expanduser('~'), '.psgen/payload')

    payload_files = []

    if path.exists(builtin_payload_path):
        for filename in glob.iglob(path.join(builtin_payload_path, '*.ps1')):
            payload_files.append(filename)

    if path.exists(local_payload_path):
        for filename in glob.iglob(path.join(local_payload_path, '*.ps1')):
            payload_files.append(filename)

    payloads = []
    for filename in payload_files:
        with open(filename, "r") as f:
            content = f.read()
            sections = content.split("##########", 3)
            if len(sections) != 3:
                print("[-] Error parsing payload [ %s ]" % filename)
                continue

            metadata = sections[1]
            script = sections[2]

            try:
                payload = yaml.safe_load(metadata)
            except yaml.YAMLError as e:
                print("[-] Error parsing payload [ %s ]" % filename)
            
            if "Name" not in metadata or "Author" not in metadata or "Description" not in metadata or "Options" not in metadata:
                print("[-] Error parsing payload [ %s ]" % filename)
                continue

            payload["Script"] = script

            payloads.append(payload)
    return payloads

def get_payload(payloads, name):
    for payload in payloads:
        if payload["Name"].lower() == name.lower():
            return payload
    
    return None

def escape(script):
    return script.replace('"', '\\"')

def encode(script):
    return base64.b64encode(script.encode('utf16')[2:]).decode()

def main():
    parser = argparse.ArgumentParser(description=psgen.__doc__)
    parser.add_argument('payload', nargs='?', metavar='payload', type=str,
                    help='Powershell Payload')
    parser.add_argument('options', nargs='*', metavar='options', type=str,
                    help='Payload Options')
    parser.add_argument('-l', '--list', action='store_true',
                    help='List Payloads')
    parser.add_argument('-r', '--raw', action='store_true',
                    help='Output with raw Powershell payload')

    args = parser.parse_args()
    payloads = load_payloads()
    
    print()
    if args.list:
        headers = ["Name", "Author", "Description", "Options"]
        data = []
        for payload in payloads:
            options = payload["Options"]
            options_str = ""
            for option in options:
                options_str += "%s => '%s', " % (option, options[option])
                
            data.append([payload["Name"], payload["Author"], payload["Description"], options_str])
        print("Powershell Payloads")
        print("===================")
        print(tabulate(data, headers=headers, tablefmt='orgtbl'))
        print()
    elif args.payload:
        payload = get_payload(payloads, args.payload)
        if not payload:
            print("[-] Error payload not found [ %s ]" % args.payload)
            sys.exit(1)

        input_options = {}
        if args.options:
            input_options = load_options(args.options)
        
        options_str = ""
        for option in payload["Options"]:
            if option not in input_options:
                input_options[option] = input("Set option [ %s ]: " % option)
            
            options_str += "%s=%s, " % (option, repr(input_options[option]))

        template = Template(payload["Script"])
        script = template.render(input_options)
        script = minify(script)

        print("Payload Detail")
        print("==============")
        print("Payload Name: %s" % payload["Name"])
        print("Payload Author: %s" % payload["Author"])
        print("Payload Description: %s" % payload["Description"])
        print("Payload Options: %s" % options_str)
        print()
        print("Payload Output")
        print("==============")
        if args.raw:
            print("powershell.exe -C \"%s\"" % escape(script))
        else:
            print("powershell.exe -E %s" % encode(script))
        print()
        pass
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
