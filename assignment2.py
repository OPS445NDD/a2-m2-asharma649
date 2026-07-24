#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Winter 2023
Program: assignment2.py 
Author: "Student Name"
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 

'''

import argparse
import os, sys

def parse_command_args() -> object:
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )

    parser.add_argument("-H", "--human-readable",
                        action="store_true",
                        help="Prints sizes in human readable format")

    parser.add_argument("-l", "--length",
                        type=int,
                        default=20,
                        help="Specify the length of the graph. Default is 20.")

    parser.add_argument("program",
                        type=str,
                        nargs='?',
                        help="if a program is specified, show memory use of all associated processes. Show only total use if not.")

    return parser.parse_args()


def percent_to_graph(percent: float, length: int=20) -> str:
    pass


def get_sys_mem() -> int:
    pass


def get_avail_mem() -> int:
    pass


def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    result = os.popen(f'pidof {app_name}').read().strip()
    if result == "":
        return []
    return result.split()


def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the Resident memory used"
    total_rss = 0
    try:
        with open(f"/proc/{proc_id}/smaps", "r") as f:
            for line in f:
                if line.startswith("Rss:"):
                    parts = line.split()
                    total_rss += int(parts[1])  # value in kB
    except FileNotFoundError:
        return 0
    return total_rss


def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result


if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        pass
    else:
        pass

