#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "jhoelzer"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true")
    parser.add_argument("text", help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)

    namespace = parser.parse_args(args)

    if namespace.upper:
        namespace.text = namespace.text.upper()
    if namespace.lower:
        namespace.text = namespace.text.lower()
    if namespace.title:
        namespace.text = namespace.text.title()
    return namespace.text


if __name__ == '__main__':
    print(main(sys.argv[1:]))