#!/usr/bin/env python3

import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def parse_line(line):
    parts = line.split()
    if len(parts) != 7:
        return None, None
    ip_address, _, _, status_code, file_size = parts[:2] + parts[3:6]
    if not status_code.isdigit():
        return None, None
    return int(status_code), int(file_size)

def main():
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line.strip())
            if status_code is None or file_size is None:
                continue
            total_size += file_size
            status_counts[status_code] += 1
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

