#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import re
import sys

so = '^((?:[0-9]{1,3}\.){3}[0-9]{1,3}) - (\[.+\]) '
st = '"GET \/projects\/260 HTTP\/1.1" (\d+) (\d+)'
regex = r'{}{}'.format(so, st)
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        if re.match(regex, line):
            counter += 1
            res = re.search(regex, line)
            total_size += int(res.group(4))
            cache[res.group(3)] += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
