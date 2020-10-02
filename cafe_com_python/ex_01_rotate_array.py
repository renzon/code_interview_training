"""
Enunciado do exercício:
https://www.programcreek.com/2015/03/rotate-array-in-java/

Métodos a serem memorizados

Lista:
    >>> list('banana')
    ['b', 'a', 'n', 'a', 'n', 'a']
    >>> lst = [1, 2]
    >>> copia = list(lst)
    >>> copia
    [1, 2]
    >>> copia is lst
    False


String:
    >>> ''.join(['b', 'a', 'n', 'a', 'n', 'a'])
    'banana'
    >>> '-'.join(['b', 'a', 'n', 'a', 'n', 'a'])
    'b-a-n-a-n-a'
    >>> str('banana')
    'banana'


Métodos em comum:
    >>> s = 'banana'
    >>> lst=['b', 'a', 'n', 'a', 'n', 'a']
    >>> s[0], lst[0]
    ('b', 'b')
    >>> s[-1], lst[-1]
    ('a', 'a')
    >>> len(s), len(lst)
    (6, 6)
    >>> s[2:5],lst[2:5]  # O(final - inicial)
    ('nan', ['n', 'a', 'n'])
    >>> s[:5],lst[:5]
    ('banan', ['b', 'a', 'n', 'a', 'n'])
    >>> s[4:],lst[4:]
    ('na', ['n', 'a'])
    >>> sorted(s), sorted(lst)  # O(nlog(n))   Tim Sort
    (['a', 'a', 'a', 'b', 'n', 'n'], ['a', 'a', 'a', 'b', 'n', 'n'])
    >>> lst
    ['b', 'a', 'n', 'a', 'n', 'a']
    >>> lst.sort()
    >>> lst
    ['a', 'a', 'a', 'b', 'n', 'n']
"""
from typing import List


def rotacionar(lista: List, k: int):
    """
    >>> lista = [1,2,3,4,5,6,7]
    >>> list(rotacionar(lista, 3))
    [5, 6, 7, 1, 2, 3, 4]
    >>> for elemento in rotacionar(lista, 1):
    ...     print(elemento)
    ...
    7
    1
    2
    3
    4
    5
    6
    >>> next(iter(rotacionar(lista, 2)))
    6

    :param iteravel:
    :param k:
    :return:
    """
    primeira_fatia = lista[-k:]  # O(n) em tempo e em espaço
    segunda_fatia = lista[:-k]
    return primeira_fatia + segunda_fatia
