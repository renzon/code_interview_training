#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478
from itertools import islice

matrix = []

for i in range(101):
    matrix.append(tuple('{:>3}'.format(abs(i - j) + 1) for j in range(101)))

while True:
    size = int(input())
    if size == 0:
        break

    for line, _ in zip(matrix, range(size)):
        elements = islice(line, size)
        print(' '.join(elements))
    print()
