# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from itertools import product

BLACK = 'B'
WHITE = 'W'
EMPTY = 'E'

board_white_unfinished = [
    [BLACK, WHITE, BLACK, EMPTY],
    [WHITE, WHITE, WHITE, EMPTY],
    [WHITE, WHITE, WHITE, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY]
]

board_white_finished = [
    [BLACK, WHITE, BLACK, BLACK],
    [WHITE, WHITE, WHITE, BLACK],
    [WHITE, WHITE, WHITE, BLACK],
    [BLACK, BLACK, BLACK, BLACK]
]


def has_move(board, line, column):
    m = len(board)
    if m == 0:
        raise Exception('Should have at least one line')
    n = len(board[0])
    if n == 0:
        raise Exception('Should have at least one column')

    def neighbors(line, column):
        def neighbor_range(current, max_value):
            return range(max(0, current - 1), min(max_value, current + 2))

        return (
            (a, b) for a, b in
            product(neighbor_range(line, m), neighbor_range(column, n))
            if (a, b) != (line, column)
        )

    color = board[line][column]

    if color is EMPTY:
        raise Exception('Should be an colored position')

    def neighbors_of_same_color(line, column):
        return ((a, b) for a, b in neighbors(line, column) if
                board[a][b] == color)

    def has_empty_neighbor(line, column):
        return any(board[l][c] == EMPTY for l, c in
            neighbors(line, column))

    # O(m*n) in time and space
    visited = set()
    to_be_visited = [(line, column)]

    while to_be_visited:
        current_line, current_column = to_be_visited.pop()
        if has_empty_neighbor(current_line, current_column):
            return True
        visited.add((current_line, current_column))
        to_be_visited.extend(
            (a, b) for a, b in
            neighbors_of_same_color(current_line, current_column)
            if (a, b) not in visited
        )
    return False


print(has_move(board_white_unfinished, 1, 1))

print(has_move(board_white_finished, 1, 1))
