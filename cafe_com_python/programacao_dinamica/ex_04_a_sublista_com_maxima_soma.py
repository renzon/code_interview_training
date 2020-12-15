"""
Encontra a sublista de uma lista de numeros que possui a maior soma

Enunciado:
https://www.programcreek.com/2013/02/leetcode-maximum-subarray-java/

"""
from numbers import Number
from typing import List, Tuple, Iterable


def sublista_de_maxima_soma_quadratico(lista_de_numeros: List[Number]) -> Tuple[List, Number]:
    """
    >>> sublista_de_maxima_soma_quadratico([])
    ([], 0)
    >>> sublista_de_maxima_soma_quadratico([1, 1, 2, 3])
    ([1, 1, 2, 3], 7)
    >>> sublista_de_maxima_soma_quadratico([-1, 1, 1, 2, 3])
    ([1, 1, 2, 3], 7)
    >>> sublista_de_maxima_soma_quadratico([-1])
    ([], 0)
    >>> sublista_de_maxima_soma_quadratico([0.1])
    ([0.1], 0.1)
    >>> sublista_de_maxima_soma_quadratico([-2,1,-3,4,-1,2,1,-5,4])
    ([4, -1, 2, 1], 6)


    :param lista_de_numeros:
    :return:
    """
    sublista = max(gerar_sub_listas(lista_de_numeros), key=sum)
    return sublista, sum(sublista)


def gerar_sub_listas(lista: List[Number]) -> Iterable[List[Number]]:
    """
    >>> list(gerar_sub_listas([]))
    [[]]
    >>> list(gerar_sub_listas([1]))
    [[], [1]]
    >>> list(gerar_sub_listas([1, 2]))
    [[], [1], [1, 2], [2]]

    :param lista:
    :return:
    """
    yield []
    for i, _ in enumerate(lista):
        for j in range(i + 1, len(lista) + 1):
            yield lista[i:j]

    # tamanho lista for 5
    # 1, 2, 3, 4
    # 2, 3, 4
    # 3, 4
    # 4,

    # a(n) = 1 + 1*(n-1)

    # (1 + 1+(n-1))*n/2 -> (n-1) * n /2 -> (n**2 -n)/2 -> O((n**2 -n)/2) -> Quadrático


def sublista_de_maxima_soma(lista_de_numeros: List[Number]) -> Tuple[List, Number]:
    """
    >>> sublista_de_maxima_soma([])
    ([], 0)
    >>> sublista_de_maxima_soma([1, 1, 2, 3])
    ([1, 1, 2, 3], 7)
    >>> sublista_de_maxima_soma([-1, 1, 1, 2, 3])
    ([1, 1, 2, 3], 7)
    >>> sublista_de_maxima_soma([-1])
    ([], 0)
    >>> sublista_de_maxima_soma([0.1])
    ([0.1], 0.1)
    >>> sublista_de_maxima_soma([-2,1,-3,4,-1,2,1,-5,4])
    ([4, -1, 2, 1], 6)


    :param lista_de_numeros:
    :return:
    """

    indice_inicial = 0
    indice_final = 0
    soma_maxima = 0
    soma_atual = 0
    for indice, numero in enumerate(lista_de_numeros):
        soma_atual += numero
        if soma_atual > 0:
            if soma_atual > soma_maxima:
                soma_maxima = soma_atual
                indice_final = indice + 1
        else:
            indice_inicial = indice + 1
            soma_atual = 0

    return lista_de_numeros[indice_inicial:indice_final], soma_maxima
