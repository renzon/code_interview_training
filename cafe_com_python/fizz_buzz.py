from collections import deque


def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz


    :param n:
    :return:
    """
    deque
    for i in range(1, n + 1):  # i=1  n=6
        resultado = ''

        if i % 2 == 0:
            resultado = 'fizz'
        if i % 3 == 0:
            resultado += 'buzz'

        resultado = resultado if resultado != '' else i
        print(resultado)  # 1  fizz 3 fizz 5 fizz
