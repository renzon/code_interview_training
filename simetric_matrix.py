#!/usr/bin/env python3
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478
import sys

while True:
    size = int(sys.argv[1])
    if not (0 < size < 100):
        break

    for i in range(size):
        for j in range(size):
            item = abs(i - j) + 1
            print('  %i' % item, end="")
        print()
    print()
