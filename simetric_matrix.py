#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478

matrix = tuple(' '.join('{:>3}'.format(abs(i - j) + 1) for j in range(101)) for i in range(101))

while True:
    size = int(input())
    if size == 0:
        break
    width = 4 * size - 1
    for i in range(size):
        print(matrix[i][:width])
    print()
