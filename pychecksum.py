#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  pychecksum.py v0.1
#
#  Copyright 2020, The JJ duo
#

import logging
import argparse
import json



def check_file(data):
    print(data)

def main():
    """Main program function."""

    # Logging config and start
    logging.basicConfig(filename='pychecksum.log', level=logging.DEBUG)
    logging.debug('---------- PYCHECKSUM START -----------')

    # Create a parser for args
    parser = argparse.ArgumentParser(
        description='Verify checksum of files in current directory.')

    # Add an argument
    parser.add_argument('file', help='File name.')

    # Parse arguments
    args = parser.parse_args()

    # Log the args
    logging.debug(f'Arguments: {args.file}')

    # Load json file
    with open(args.file) as jsonfile:
        try:
            data = json.load(jsonfile)
            print(data)
        except ValueError as error:
            print(f'Not a valid JSON file. Error {error}')
            quit()
    
    # Check if there are files
    num_of_files = len(data["files"])
    if (len(data["files"]) < 1) and data["files"]:
        print('No files to process.')
        quit()

    for x in data["files"]:
        check_file(x)

    


if __name__ == "__main__":
    main()
