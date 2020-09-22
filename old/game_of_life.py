from itertools import product
from typing import List

initial_board = [
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 0],
]

steps = [
    [
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
    ],
    [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],

    ],

    [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 0, 0],

    ],

    [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
    ],

    [
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
    ]
]


class Game:
    def __init__(self, board: List[List[int]]):
        self.current_board = board
        self._rows = len(board)
        self._columns = len(board[0])

    def evolve(self):
        new_board = [[0] * self._columns for _ in range(self._rows)]
        for row, column in product(range(self._rows), range(self._columns)):
            neighbors_sum = sum(self._neighbors(row, column))
            if neighbors_sum == 3 or (neighbors_sum == 2 and self.current_board[row][column] == 1):
                new_board[row][column] = 1
        self.current_board = new_board
        return new_board

    def _neighbors(self, row, column):
        min_row = max(0, row - 1)
        max_row = min(self._rows, row + 2)
        min_column = max(0, column - 1)
        max_column = min(self._columns, column + 2)
        for r, c in product(range(min_row, max_row), range(min_column, max_column)):
            if (r, c) != (row, column):
                yield self.current_board[r][c]


def test_game_of_life():
    game = Game(initial_board)

    for step in steps:
        game.evolve()
        assert game.current_board == step
