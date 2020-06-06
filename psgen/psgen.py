#!/usr/bin/env python

import argparse
import psgen
import sys
from os import path

def main():
    parser = argparse.ArgumentParser(description=psgen.__doc__)
    parser.add_argument('payload', metavar='payload', type=str,
                    help='Powershell Payload')

    args = parser.parse_args()
    if not args.payload:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
