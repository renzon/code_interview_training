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


class MoveResolver:

    def __init__(self, board):
        self.board = board

    def has_move(self, x, y):
        """Returns a_com_fatia_linar boolean indicating if color present on position x,y still has available move

        :param x: position x
        :param y: position y
        :return: bool
        """
        origin = x, y
        return any(self.get_color(x, y) == EMPTY for x, y in self.edge_neighbours(origin))

    def find_edge_point(self, x, y):
        color = self.get_color(x, y)
        if color == EMPTY:
            raise Exception('Can only calculate possible moves of non empty points')
        edge_x = x
        for edge_x in range(x, -1, -1):
            if color != self.get_color(edge_x, y):
                break
        return edge_x, y

    def get_color(self, x, y):
        return self.board[x][y]

    def scan_edge(self, origin):
        first_edge = self.find_edge_point(*origin)
        yield first_edge

        first_edge_neighbours = set(self.calculate_edge_neighbours(first_edge))
        yield from first_edge_neighbours

        current_edge = next(self.calculate_neighbours(first_edge), None)
        previous_edge = first_edge

        while current_edge is not None:
            current_edge_neighbours = set(self.calculate_edge_neighbours(current_edge))
            previous_edge_neighbours = set(self.calculate_edge_neighbours(previous_edge))
            current_edge_neighbours -= previous_edge_neighbours
            current_edge_neighbours -= first_edge_neighbours
            yield from current_edge_neighbours
            previous_edge = current_edge
            current_edge = next(iter(current_edge_neighbours), None)

    def edge_neighbours(self, point):
        for edge in self.scan_edge(point):
            yield from self.calculate_neighbours(edge)

    def calculate_neighbours(self, point):
        x, y = point

        feasible_x_range = {max(0, x - 1), x, min(len(self.board) - 1, x + 1)}
        feasible_y_range = {max(0, y - 1), y, min(len(self.board[0]) - 1, y + 1)}

        for neihgbour_candidate in product(feasible_x_range, feasible_y_range):
            if neihgbour_candidate != point:
                yield neihgbour_candidate

    def calculate_edge_neighbours(self, edge):
        color = self.get_color(*edge)

        def is_border(x, y):
            return x == 0 or x == (len(self.board) - 1) or y == 0 or y == (len(self.board[0]) - 1)

        for edge_candidate in self.calculate_neighbours(edge):
            if color == self.get_color(*edge_candidate) and (
                    is_border(*edge_candidate) or any(self.get_color(x, y) != color for x, y in
                                                      self.calculate_neighbours(edge_candidate))):
                yield edge_candidate


print(MoveResolver(board_white_finished).has_move(1, 1))
print(MoveResolver(board_white_unfinished).has_move(1, 1))
