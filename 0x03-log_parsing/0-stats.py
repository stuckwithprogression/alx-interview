#!/usr/bin/python3
"""
Log Parsing Script
This script reads log data from standard input (stdin), parses the log entries,
and tracks the frequency of various HTTP status codes and the cumulative file
size of all processed log entries. The script prints the cumulative file size
and status code counts after every 10 lines processed and upon termination
(normal or via KeyboardInterrupt).
Log entries are expected to have a format that includes HTTP status codes and
file sizes. The supported HTTP status codes being tracked are:
- 200: OK
- 301: Moved Permanently
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 405: Method Not Allowed
- 500: Internal Server Error
"""

import re
import sys

line_counter = 0
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0,
                      405: 0, 500: 0}


def print_status_counts(status_counts, file_size):
    """
    Prints the total file size and the count of each HTTP status code.
    Args:
        status_counts (dict): A dictionary with HTTP status codes as
        keys and their counts as values.
        file_size (int): The cumulative size of files processed.
    """
    print("File size: {}".format(file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] != 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_line = re.split('- |"|"| " " ', str(line))
            status_code_and_file_size = split_line[-1]
            if line_counter != 0 and line_counter % 10 == 0:
                print_status_counts(status_code_counts, total_file_size)
            line_counter += 1
            try:
                status_code = int(status_code_and_file_size.split()[0])
                file_size = int(status_code_and_file_size.split()[1])
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                total_file_size += file_size
            except (IndexError, ValueError):
                pass
        print_status_counts(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        print_status_counts(status_code_counts, total_file_size)
        raise
