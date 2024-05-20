#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import re


def print_status(status_codes, total_size):
    """Prints metrics"""
    print("Total file size: {:d}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{}: {:d}".format(code, count))


def parse_line(line):
    """Parses a log line and returns status code and file size"""
    match = re.match(r".*\".*\" (\d+) (\d+)$", line)
    if match:
        status_code, size = match.groups()
        return status_code, int(size)
    return None, None


def main():
    """Main function"""
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
    total_size = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            if count % 10 == 0:
                print_status(status_codes, total_size)

            status_code, size = parse_line(line)
            if size is not None:
                total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1

        print_status(status_codes, total_size)

    except KeyboardInterrupt:
        print_status(status_codes, total_size)
        raise


if __name__ == "__main__":
    main()
