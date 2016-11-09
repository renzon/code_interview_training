def _tribonacci_iter(n, e_1, e_2, e_3):
    if n == 0:
        return e_3
    return _tribonacci_iter(n - 1, e_2, e_3, e_3 + e_2 + e_1)


def tribonacci(n, signature=None):
    signature = signature or (1, 1, 1)
    if len(signature) != 3:
        raise Exception('signature must have 3 elements or be None')
    if n < 0:
        return signature[0]
    elif n <= 3:
        return signature[n - 1]
    return _tribonacci_iter(n - 3, *signature)


for n in range(1, 10):
    print(n, tribonacci(n))
