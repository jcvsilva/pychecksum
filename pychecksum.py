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
import os
import hashlib

def check_file(data):
    print(f'Filename: {data["filename"]}')
    print(f'Filename: {data["MD5"]}')

    # Check if file exist
    if os.path.exists(data["filename"]) :
        with open(data["filename"], 'rb') as file:
            file_hash = hashlib.md5()
            while True:
                block = file.read(8192)
                if not block:
                    break
                file_hash.update(block)
        print(file_hash.hexdigest())
        if file_hash.hexdigest() == data["MD5"]:
            return True
        else:
            return False
    else:
        print("File don't exist.")
        return False


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
            logging.debug(f'json data: {data}')
        except ValueError as error:
            print(f'Not a valid JSON file. Error {error}')
            quit()
    
    # Check if there is a files keyin JSON
    if 'files' not in data:
        print('Not a valid JSON file. files key do not exist')
        quit()
    
    # Check if there are files
    if len(data["files"]) < 1 :
        print('No files to process.')
        quit()

    for x in data["files"]:
        if check_file(x):
            print(f"MD5 do ficheiro {x['filename']} está correcto.")
        else:
            print(f"MD5 do ficheiro {x['filename']} está errado.")


if __name__ == "__main__":
    main()
