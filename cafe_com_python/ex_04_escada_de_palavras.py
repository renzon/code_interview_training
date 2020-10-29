"""
Enunciado do exercício:

https://www.programcreek.com/2012/12/leetcode-word-ladder/

"""
from collections import deque


class TransformacaoNaoEncontrada(Exception):
    pass

def tamanho_da_sequencia_de_transformacao(palavra_inicio: str, palavra_final: str, conjunto_de_palavras: set) -> int:
    """
    >>> tamanho_da_sequencia_de_transformacao('cog', 'cog', {"hot","dot","dog","lot","log"})
    1
    >>> tamanho_da_sequencia_de_transformacao('dog', 'cog', {"hot","dot","dog","lot","log"})
    2
    >>> tamanho_da_sequencia_de_transformacao('dot', 'cog', {"hot","dot","dog","lot","log"})
    3
    >>> tamanho_da_sequencia_de_transformacao('hot', 'cog', {"hot","dot","dog","lot","log"})
    4
    >>> tamanho_da_sequencia_de_transformacao('hit', 'cog', {"hot","dot","dog","lot","log"})
    5
    >>> tamanho_da_sequencia_de_transformacao('fat', 'cog', {"hot","dot","dog","lot","log"})
    Traceback (most recent call last):
    ...
    ex_04_escada_de_palavras.TransformacaoNaoEncontrada: Impossível achar um transformação de fat para cog
    >>> tamanho_da_sequencia_de_transformacao('hit', 'fat', {"hot","dot","dog","lot","log"})
    Traceback (most recent call last):
    ...
    ex_04_escada_de_palavras.TransformacaoNaoEncontrada: Impossível achar um transformação de fat para cog


    O(n**n) para memória e tempo de execução
    :param palavra_inicio:
    :param palavra_final:
    :param conjunto_de_palavras:
    :return:
    """
    conjunto_de_palavras.add(palavra_final)
    tamanho_do_menor_caminho = 1
    fila_de_nos = deque()
    fila_de_nos.append((palavra_inicio, tamanho_do_menor_caminho))

    while len(fila_de_nos) >= 1:
        palavra_corrente, tamanho_do_menor_caminho = fila_de_nos.popleft()
        if palavra_corrente == palavra_final:
            return tamanho_do_menor_caminho
        else:
            for palavra_do_conjunto in conjunto_de_palavras:
                if possui_apenas_uma_letra_diferente(palavra_do_conjunto, palavra_corrente):
                    fila_de_nos.append((palavra_do_conjunto, tamanho_do_menor_caminho + 1))

    raise TransformacaoNaoEncontrada(f'Impossível achar um transformação de {palavra_inicio} para {palavra_final}')


def possui_apenas_uma_letra_diferente(palavra: str, outro_palavra: str) -> bool:
    """

    >>> possui_apenas_uma_letra_diferente('dog', 'cog')
    True
    >>> possui_apenas_uma_letra_diferente('too', 'tot')
    True
    >>> possui_apenas_uma_letra_diferente('too', 'tott')
    False
    >>> possui_apenas_uma_letra_diferente('dig', 'cog')
    False
    >>> possui_apenas_uma_letra_diferente('dig', 'cog')
    False

    :param palavra:
    :param outro_palavra:
    :return:
    """
    if len(palavra) != len(outro_palavra):
        return False
    return sum(1 for a, b in zip(palavra, outro_palavra) if a != b) == 1
