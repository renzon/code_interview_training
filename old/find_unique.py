# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    a, b = arr[0], arr[1]
    if a != b:
        return a if b == arr[2] else b
    repeated = a
    for c in arr:
        if c != repeated:
            return c
