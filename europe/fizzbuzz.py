"""
    >>> fizzbuzz(7)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz
    7
    >>> fizzbuzz(2)
    1
    fizz
"""


def fizzbuzz(n):
    for i in range(1, n + 1): # i= 6, resultado='fizzbuzz', n=7
        resultado = ''
        if i % 2 == 0:
            resultado = 'fizz'
        if i % 3 == 0:
            resultado += 'buzz'
        if resultado == '':
            resultado = i
        print(resultado)
