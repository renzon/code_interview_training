"""
Enunciado:

https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/https://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/

"""
from itertools import islice
from numbers import Number


def mediana_de_duas_listas_linear(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas_linear([1], [2])
    1.5
    >>> mediana_de_duas_listas_linear([1], [2, 3000])
    2
    >>> mediana_de_duas_listas_linear([1, 3], [2, 3000])
    2.5

    Complexidade de tempo de execução: O(n+m)
    Complexidade de memória: O(1)


    :param a:
    :param b:
    :return:
    """
    m = len(a)
    n = len(b)
    elementos_fundidos = fundir(a, b)
    tamanho = m + n

    indice_do_elemento_do_meio = tamanho // 2
    if tamanho % 2 == 1:
        segunda_metade = islice(
            elementos_fundidos, indice_do_elemento_do_meio, indice_do_elemento_do_meio + 1)
        return next(iter(segunda_metade))
    segunda_metade = islice(
        elementos_fundidos, indice_do_elemento_do_meio - 1, indice_do_elemento_do_meio + 1)
    iter_metade_maior = iter(segunda_metade)
    return (next(iter_metade_maior) + next(iter_metade_maior)) / 2


def fundir(a, b):
    iter_a = iter(a)
    iter_b = iter(b)
    elemento_atual_de_a = next(iter_a)
    elemento_atual_de_b = next(iter_b)
    while True:
        if elemento_atual_de_a > elemento_atual_de_b:
            yield elemento_atual_de_b
            try:
                elemento_atual_de_b = next(iter_b)
            except StopIteration:
                yield elemento_atual_de_a
                break
        else:
            yield elemento_atual_de_a
            try:
                elemento_atual_de_a = next(iter_a)
            except StopIteration:
                yield elemento_atual_de_b
                break

    yield from iter_a
    yield from iter_b


def mediana_de_duas_listas(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas([1], [])
    1
    >>> mediana_de_duas_listas([1], [2])
    1.5
    >>> mediana_de_duas_listas([1], [2, 3000])
    2
    >>> mediana_de_duas_listas([1, 3], [2, 3000])
    2.5

    Complexidade de tempo de execução: O((n+m)log(n+n))
    Complexidade de memória: O(n+m)


    :param a:
    :param b:
    :return:
    """
    lista_concatenada = a + b
    return mediana(lista_concatenada)


def mediana(lista: list) -> Number:
    """
    >>> mediana([1])
    1
    >>> mediana([1, 2])
    1.5
    >>> mediana([1, 3000, 2])
    2
    >>> mediana([1, 3000, 2, 3])
    2.5


    :param lista:
    :return:
    """
    lista.sort()
    return mediana_de_lista_ordenada(lista)


def mediana_de_lista_ordenada(lista):
    tamanho = len(lista)
    indice_do_elemento_do_meio = tamanho // 2
    if tamanho % 2 == 1:
        return lista[indice_do_elemento_do_meio]
    return (lista[indice_do_elemento_do_meio] + lista[indice_do_elemento_do_meio - 1]) / 2
