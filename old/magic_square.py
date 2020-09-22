"""
Magic square has all columns, lines and diagonals with same sum
"""
from itertools import permutations


def get_line_sum(line_index, square, square_side):
    return sum(square[i] for i in range(line_index * square_side, (line_index + 1) * square_side))


def get_column_sum(column_index, square, square_side):
    return sum(square[i] for i in range(column_index, len(square), square_side))


def get_same_index_diagonal(square, square_side):
    sum = 0
    diagonal_index = 0
    while diagonal_index < len(square):
        sum += square[diagonal_index]
        diagonal_index += square_side + 1
    return sum


def get_diff_index_diagonal(square, square_side):
    sum = 0
    diagonal_index = len(square) - square_side
    while diagonal_index > 0:
        sum += square[diagonal_index]
        diagonal_index -= square_side - 1
    return sum


def is_magic(square, square_side):
    line_sum = get_line_sum(0, square, square_side)
    for line_index in range(1, square_side):
        if line_sum != get_line_sum(line_index, square, square_side):
            return False
    for column_index in range(square_side):
        if line_sum != get_column_sum(column_index, square, square_side):
            return False
    if line_sum != get_same_index_diagonal(square, square_side):
        return False
    if line_sum != get_diff_index_diagonal(square, square_side):
        return False
    return True


def magic_squares(square_side):
    numbers = list(range(1, (square_side ** 2) + 1))
    yield from (square for square in permutations(numbers) if is_magic(square, square_side))


def test_magic_square_3():
    magic_square_3_x_3 = (8, 3, 4, 1, 5, 9, 6, 7, 2)
    assert is_magic(magic_square_3_x_3, 3)
    assert magic_square_3_x_3 in list(magic_squares(3))


def test_not_magic_square_3():
    not_magic_square_3_x_3 = (3, 8, 4, 1, 5, 9, 6, 7, 2)
    assert not is_magic(not_magic_square_3_x_3, 3)
    assert not_magic_square_3_x_3 not in list(magic_squares(3))
