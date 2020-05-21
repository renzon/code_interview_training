from itertools import product


def switch(input_matrix, switch_index):
    matrix_size = len(input_matrix)
    result_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    regular_indexes = product(range(matrix_size), range(matrix_size))
    switch_indexes = product(switch_index, switch_index)
    for (to_i, to_j),(from_i, from_j) in zip(regular_indexes, switch_indexes):
        result_matrix[to_i][to_j]=input_matrix[from_i][from_j]
    return result_matrix


def test_matrix_switch():
    input_matrix = [
        [25000, 0, -25000, 0, 0, 0],
        [0, 33, 0, 0, 0, -33],
        [-25000, 0, 37800, -9600, -12800, 9600],
        [0, 0, -9600, 7200, 9600, -7200],
        [0, 0, -12800, 9600, 12800, -9600],
        [0, -33, 9600, -7200, -9600, 40533],
    ]
    expected_matrix = [
        [37800, -9600, -25000, 0, -12800, 9600],
        [-9600, 7200, 0, 0, 9600, -7200],
        [-25000, 0, 25000, 0, 0, 0],
        [0, 0, 0, 33, 0, -33],
        [-12800, 9600, 0, 0, 12800, -9600],
        [9600, -7200, 0, -33, -9600, 40533],
    ]

    assert switch(input_matrix, [2, 3, 0, 1, 4, 5]) == expected_matrix
