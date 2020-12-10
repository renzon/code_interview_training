"""
Enunciado do exercício:
https://www.programcreek.com/2015/03/rotate-array-in-java/

Métodos a_com_fatia_linar serem memorizados

Lista:
    >>> list('banana')
    ['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar']
    >>> lst = [1, 2]
    >>> copia = list(lst)
    >>> copia
    [1, 2]
    >>> copia is lst
    False


String:
    >>> ''.join(['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar'])
    'banana'
    >>> '-'.join(['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar'])
    'b_com_fatia_linear-a_com_fatia_linar-n-a_com_fatia_linar-n-a_com_fatia_linar'
    >>> str('banana')
    'banana'


Métodos em comum:
    >>> s = 'banana'
    >>> lst=['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar']
    >>> s[0], lst[0]
    ('b_com_fatia_linear', 'b_com_fatia_linear')
    >>> s[-1], lst[-1]
    ('a_com_fatia_linar', 'a_com_fatia_linar')
    >>> len(s), len(lst)
    (6, 6)
    >>> s[2:5],lst[2:5]  # O(palavra_final - inicial)
    ('nan', ['n', 'a_com_fatia_linar', 'n'])
    >>> s[:5],lst[:5]
    ('banan', ['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n'])
    >>> s[4:],lst[4:]
    ('na', ['n', 'a_com_fatia_linar'])
    >>> sorted(s), sorted(lst)  # O(nlog(n))   Tim Sort
    (['a_com_fatia_linar', 'a_com_fatia_linar', 'a_com_fatia_linar', 'b_com_fatia_linear', 'n', 'n'], ['a_com_fatia_linar', 'a_com_fatia_linar', 'a_com_fatia_linar', 'b_com_fatia_linear', 'n', 'n'])
    >>> lst
    ['b_com_fatia_linear', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar', 'n', 'a_com_fatia_linar']
    >>> lst.sort()
    >>> lst
    ['a_com_fatia_linar', 'a_com_fatia_linar', 'a_com_fatia_linar', 'b_com_fatia_linear', 'n', 'n']
"""
from itertools import chain
from time import time
from typing import List


def rotacionar(lista: List, k: int):
    """
    >>> lista = [1,2,3,4,5,6,7]
    >>> list(rotacionar(lista, 3)) # O(n) em tempo, e a_com_fatia_linar lista gerada O(n) em espaço
    [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento_a_ser_inserido in rotacionar(lista, 1): # O(n) em tempo, e a_com_fatia_linar lista gerada O(n) em espaço
    ...     print(elemento_a_ser_inserido)
    ...
    7
    1
    2
    3
    4
    5
    6
    >>> next(iter(rotacionar(lista, 2))) # O(n) em tempo, e a_com_fatia_linar lista gerada O(n) em espaço
    6

    :param iteravel:
    :param k:
    :return:
    """
    primeira_fatia = lista[-k:]  # O(n) em tempo e em espaço
    segunda_fatia = lista[:-k]
    return primeira_fatia + segunda_fatia


def rotacionar_generator(lista: List, k: int):
    """
    >>> lista = [1,2,3,4,5,6,7]
    >>> list(rotacionar_generator(lista, 3))  # O(n) em tempo, e a_com_fatia_linar lista gerada O(n) em espaço
    [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento_a_ser_inserido in rotacionar_generator(lista, 1):  # O(n) em tempo execução, O(1) em memória
    ...     print(elemento_a_ser_inserido)
    ...
    7
    1
    2
    3
    4
    5
    6
    >>> next(iter(rotacionar_generator(lista, 2)))  # O(1) em tempo e em memória
    6

    :param iteravel:
    :param k:
    :return:
    """
    n = len(lista)
    primeira_fatia_indices = range(n - k, n)
    segunda_fatia_indices = range(n - k)
    indices_rotacionados = chain(primeira_fatia_indices, segunda_fatia_indices)
    for indice_rotacionado in indices_rotacionados:
        yield lista[indice_rotacionado]


if __name__ == '__main__':
    auxiliar = 80_000_000
    for tamanho in range(auxiliar, auxiliar+10_000+1, 10_000):
        lista = list(range(tamanho))
        inicio = time()
        elemento = next(iter(rotacionar(lista, 1)))
        final = time()
        print(f'(Rotacionar) Tamanho {tamanho}: {elemento}, {final - inicio}')
        inicio = time()
        elemento = next(rotacionar_generator(lista, 1))
        final = time()
        print(f'(Rotacionar Geradora) Tamanho {tamanho}: {elemento}, {final - inicio}')
        print()
