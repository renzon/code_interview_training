_algarism_dct = {str(n): n for n in range(10)}


def _str_to_int_rec(str, index=0, number=0):
    if index == len(str):
        return number
    digit = _algarism_dct[str[index]]
    return _str_to_int_rec(str, index + 1, number * 10 + digit)


def str_to_int(str):
    return _str_to_int_rec(str)

for i in range(1000,2000):
    print(i, str_to_int(str(i)))
