#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478


while True:
    size = int(input())
    if size == 0:
        break
    elif not (0 < size < 100):
        continue

    for i in range(size):
        for j in range(size):
            item = abs(i - j) + 1
            print('{:>3}'.format(item), end="")
        print()
    print()
2