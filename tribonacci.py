def _tribonacci_iter(e_3, e_2, e_1, n):
    if n == 0:
        return e_3
    return _tribonacci_iter(e_3 + e_2 + e_1, e_3, e_2, n - 1)


def tribonacci(n):
    if n <= 3:
        return 1
    return _tribonacci_iter(1, 1, 1, n - 3)


for n in range(1, 10):
    print(n, tribonacci(n))
