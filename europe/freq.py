"""
    >>> freq('banana')
    {'b': 1, 'a': 3, 'n': 2}
    >>> freq('aha')
    {'a': 2, 'h': 1}
"""
from functools import reduce


def freq(s):
    def contar_letra(resultado, letra):
        resultado[letra] = resultado.get(letra, 0) + 1
        return resultado

    return reduce(contar_letra, s, {})
