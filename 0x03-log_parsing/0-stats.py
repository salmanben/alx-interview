#!/usr/bin/python3
""" Log Passing """
if __name__ == '__main__':
    from sys import stdin

    total_file_size = 0
    codes = {}

    line_counts = 0

    def help_print():
        """ Helper Function to print """
        print(f"File size: {total_file_size}")
        for code, count in sorted(codes.items()):
            print(f"{code}: {count}")

    try:
        for line in stdin:
            try:
                line_parts = line.split()

                total_file_size += int(line_parts[-1])
                status = int(line_parts[-2])
                statuses = [200, 301, 400, 401, 403, 404, 405, 500]
                if status in statuses:
                    if status in codes:
                        codes[status] += 1
                    else:
                        codes[status] = 1
                    line_counts += 1

            except (ValueError, IndexError, KeyError, TypeError):
                continue
            else:
                if line_counts % 10 == 0:
                    help_print()
        help_print()
    except KeyboardInterrupt:
        help_print()
