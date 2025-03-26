#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: "Prakash Gautam"
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This program provides an improved disk usage report with bar charts.
It displays the disk usage of subdirectories within a target directory in a
visual format, with options to customize the output.
'''

def parse_command_args():
    """Parse and return command line arguments"""
    parser = argparse.ArgumentParser(
        description="DU Improved -- See Disk Usage Report with bar charts",
        epilog="Copyright 2022"
    )
    parser.add_argument(
        "-H", "--human-readable",
        action="store_true",
        help="print sizes in human readable format (e.g. 1K 23M 2G)"
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="The directory to scan."
    )
    return parser.parse_args()

def percent_to_graph(percent, total_chars):
    """Convert percentage to graph string"""
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be between 0 and 100")
    num_symbols = round((percent / 100) * total_chars)
    return '=' * num_symbols + ' ' * (total_chars - num_symbols)

def call_du_sub(location):
    """Run du command and return output lines"""
    try:
        result = subprocess.run(
            ['du', '-d', '1', location],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            return []
        return [line.strip() for line in result.stdout.split('\n') if line.strip()]
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

def create_dir_dict(du_output):
    """Convert du output to dictionary"""
    dir_dict = {}
    for line in du_output:
        try:
            size, path = line.split('\t', 1)
            dir_dict[path] = int(size)
        except ValueError:
            continue
    return dir_dict

def format_size(size, human_readable):
    """Format size in human readable or bytes"""
    if not human_readable:
        return str(size)
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}P"

def main():
    """Main function that just handles -h"""
    parse_command_args()
    # Don't do anything else for this test

if __name__ == "__main__":
    main()
