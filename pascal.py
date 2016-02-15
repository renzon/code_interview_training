# http://www.programcreek.com/2014/03/leetcode-pascals-triangle-java/
from itertools import chain


def pascal(n):
    if n <= 0:
        return
    line = (1,)
    yield line
    for i in range(n - 1):
        line_with_left_zero = chain(range(1), line)
        line_with_right_zero = chain(line, range(1))
        line = tuple(prev + v for prev, v in zip(line_with_right_zero, line_with_left_zero))
        yield line


for i in range(10):
    print(i, list(pascal(i)))
