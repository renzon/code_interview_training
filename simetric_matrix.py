#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1478


while True:
    size = int(input())
    if size == 0:
        break

    for i in range(size):
        elements = ('{:>3}'.format(abs(i - j) + 1) for j in range(size))
        print(' '.join(elements))
    print()
