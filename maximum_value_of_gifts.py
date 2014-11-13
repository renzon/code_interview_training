# http://codercareer.blogspot.com.br/2014/10/no-56-maximal-value-of-gifts.html

def max_value_of_gifts(matrix):
    m = len(matrix)  # 2
    n = len(matrix[0])  # 2
    if m == 1:
        return sum(matrix[0])
    elif n == 1:
        return sum([matrix[i][0] for i in range(m)])

    matrix_down = matrix[:-1]  # [[1,2]]

    matrix_up = [[matrix[x][y] for y in range(n - 1)] for x in range(m)]  # matrix_up=[[1],[3]]

    return matrix[-1][-1] + max(max_value_of_gifts(matrix_down),
                                max_value_of_gifts(matrix_up))  # 4 + max([[1,2]],[[1],[3]])


matrix = [[1, 10, 3, 8],
          [12, 2, 9, 6],
          [5, 7, 4, 11],
          [3, 7, 16, 5]]

print(max_value_of_gifts(matrix))
    