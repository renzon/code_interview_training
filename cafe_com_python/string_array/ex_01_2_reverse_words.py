"""
Enunciado: https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/

lista
lista.insert(indice, valor) O(tamanho - indice)
Então a_com_fatia_linar lista é uma boa estrutura para implementar uma pilha LIFO Last In First Out

Deque implmenta uma lista duplamente ligada em Python.
Esse tipo de estrutura de dados é ideal para implementar Fila - FIFO - First In First Out
Pilha


"""
from collections import deque
from itertools import chain
from typing import List, Iterable


def reverter_palavras(frase: str) -> str:
    """
    >>> reverter_palavras('the sky is blue')
    'blue is sky the'
    >>> reverter_palavras('Renzo Nuccitelli')
    'Nuccitelli Renzo'


    :param frase:
    :return:
    """
    palavras_separadas = frase.split()  # O(n + n +n)  O(n + n) -> Linear em tempo e espaço

    # return ' '.join(reversed(frase.split(' ')))
    # return ' '.join(palavras_separadas[::-1])
    return ' '.join(reversed(palavras_separadas))


def reverter_palavras_espaco_constante_se_tamanaho_da_palavra_constante(frase: str) -> Iterable:
    """
    >>> list(reverter_palavras_espaco_constante_se_tamanaho_da_palavra_constante('the sky is blue'))
    ['blue', 'is', 'sky', 'the']
    
    :param frase: 
    :return: 
    """
    palavra = deque()  # palavra: blue  O(1) em memória se o tamanho das palavras tiverem um valor máximo

    for letra in reversed(frase):
        if letra == ' ':
            yield ''.join(palavra)
            palavra.clear()
        else:
            palavra.appendleft(letra)

    yield ''.join(palavra)


def reverter_palavras_tempo_constate(frase: List) -> List:
    """
    >>> reverter_palavras_tempo_constate(
    ... ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b_com_fatia_linear', 'l', 'u', 'e'])
    ['b_com_fatia_linear', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
    e u l b_com_fatia_linear   ' ' e h t

    0 -> 12
    1 -> 13
    2 -> 14
    3 -> 11

    tamanho=3
    indice_esquerda = 3
    indice_direita= 11

    Mudança para nao espaco:
    indice_esqueda




    Primeira vez, swap do primeido da direita, com Coloar da esquerda





    :param frase:
    :return:
    """

    return frase


def reverter_espaco_constante(frase: list) -> list:
    """
    >>> reverter_espaco_constante(['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b_com_fatia_linear', 'l', 'u', 'e'])
    ['b_com_fatia_linear', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
    
    eht yks si eulb
    
     
    """
    indice_inicio_de_palavra = 0

    for indice, letra in enumerate(chain(frase, ' ')):
        if letra == ' ':
            reverter_auxiliar(frase, indice_inicio_de_palavra, indice - 1)
            indice_inicio_de_palavra = indice + 1

    reverter_auxiliar(frase, 0, len(frase) - 1)

    return frase


def reverter_auxiliar(frase: list, inicio: int, final: int) -> None:
    while inicio < final:
        frase[inicio], frase[final] = frase[final], frase[inicio]
        inicio += 1
        final -= 1
