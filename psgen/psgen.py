#!/usr/bin/env python

import argparse
import psgen
import sys
from os import path
import glob
import yaml
from tabulate import tabulate

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

            payload["script"] = script

            payloads.append(payload)
    return payloads
                
    


def main():
    parser = argparse.ArgumentParser(description=psgen.__doc__)
    parser.add_argument('payload', nargs='?', metavar='payload', type=str,
                    help='Powershell Payload')
    parser.add_argument('options', nargs='*', metavar='options', type=str,
                    help='Payload Options')
    parser.add_argument('-l', '--list', action='store_true',
                    help='List Payloads')

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
                options_str += "%s => %s\n" % (option, options[option])
                
            data.append([payload["Name"], payload["Author"], payload["Description"], options_str])
        print("Powershell Payloads")
        print("===================")
        print(tabulate(data, headers=headers, tablefmt='orgtbl'))
        print()
    elif args.payload:
        pass
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
