"""
Ache o segundo maior valor de um iterável de números.

 Perguntas importantes:

 1. A lista está ordenada
 2. Se possui elementos duplicados
"""
import bisect
import math
from numbers import Number
from typing import List, Iterable


class NaoPossuiSegundoMaiorElemento(Exception):
    pass


def encontrar_segundo_maior_elemento_lista_ordenada(lista_ordenada: List) -> Number:
    """
    >>> encontrar_segundo_maior_elemento_lista_ordenada([1, 1, 1, 1, 2, 2, 2, 3, 3, 3])
    2
    >>> encontrar_segundo_maior_elemento_lista_ordenada([1, 1, 1, 1, 2, 2, 2, 3])
    2
    >>> encontrar_segundo_maior_elemento_lista_ordenada([1, 1, 1, 1, 2, 2, 2])
    1
    >>> encontrar_segundo_maior_elemento_lista_ordenada([1, 2])
    1
    >>> encontrar_segundo_maior_elemento_lista_ordenada([-1, 2])
    -1
    >>> encontrar_segundo_maior_elemento_lista_ordenada([2, 2])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento

    O(log(n))
    >>> encontrar_segundo_maior_elemento_lista_ordenada([2])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento
    >>> encontrar_segundo_maior_elemento_lista_ordenada([])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento

    O(log(n))

    :param lista_ordenada:
    :return:
    """
    if len(lista_ordenada) == 0:
        raise NaoPossuiSegundoMaiorElemento()
    indice = bisect.bisect_left(lista_ordenada, lista_ordenada[-1])
    if indice == 0:
        raise NaoPossuiSegundoMaiorElemento()
    return lista_ordenada[indice - 1]


def encontrar_segundo_maior_elemento(iteravel: Iterable) -> Number:
    """
    >>> encontrar_segundo_maior_elemento([5, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3])
    3
    >>> encontrar_segundo_maior_elemento([1, 1, 1, 1, -1, 2, 2, 0, 2, 3])
    2
    >>> encontrar_segundo_maior_elemento([1, 1, 1, 1, 2, 2, 2])
    1
    >>> encontrar_segundo_maior_elemento([1, 2])
    1
    >>> encontrar_segundo_maior_elemento([-1, 2])
    -1
    >>> encontrar_segundo_maior_elemento([2, 2])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento

    O(log(n))
    >>> encontrar_segundo_maior_elemento([2])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento
    >>> encontrar_segundo_maior_elemento([])
    Traceback (most recent call last):
    ...
    segundo_maior_valor.NaoPossuiSegundoMaiorElemento

    O(2n) => O(n)

    :param lista_ordenada:
    :return:
    """
    iterador = iter(iteravel)
    menos_infinito = - math.inf

    # buffer = deque(maxlen=2)
    # # Candidato a elemento maximo
    # buffer.append(next(iterador, menos_infinito))
    #
    # # Encontrando candidato a segundo elemento máximo
    # for elemento in iterador:
    #     if elemento > buffer[0]:
    #         buffer.append(elemento)
    #         break
    #     elif elemento < buffer[0]:
    #         buffer.appendleft(elemento)
    #         break
    #
    # # Atualizando valores de primeiro e segundo máximo
    # for elemento in iterador:
    #     if elemento > buffer[-1]:
    #         buffer.append(elemento)
    #     elif buffer[0] < elemento < buffer[-1]:
    #         buffer.popleft()
    #         buffer.appendleft(elemento)
    #
    # if len(buffer) < 2:
    #     raise NaoPossuiSegundoMaiorElemento()
    #
    # return buffer[0]

    # Objetivo de fazer apenas um for
    valor_maximo = next(iterador, menos_infinito)
    segundo_valor_maximo = menos_infinito
    for elemento in iterador:
        if valor_maximo < elemento:
            segundo_valor_maximo = valor_maximo
            valor_maximo = elemento
        elif segundo_valor_maximo < elemento < valor_maximo:
            segundo_valor_maximo = elemento

    if segundo_valor_maximo == menos_infinito:
        raise NaoPossuiSegundoMaiorElemento()
    return segundo_valor_maximo

    # Solução do Josué
    # menos_infinito = - math.inf
    # elemento_maximo = max(iteravel, default= menos_infinito)
    # segundo_maior_elemento = menos_infinito
    # for elemento in iteravel:
    #     if elemento > segundo_maior_elemento and elemento != elemento_maximo:
    #         segundo_maior_elemento = elemento
    # if segundo_maior_elemento == menos_infinito:
    #     raise NaoPossuiSegundoMaiorElemento()
    # return segundo_maior_elemento
