"""
https://www.programcreek.com/2012/11/top-10-algorithms-for-coding-interview/

["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9    2 1 + 3 *
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Propriedades de Pilha  (Lista):

push -> Empilhar  O(1)  -> Método append
pop -> Desempilhar O(1)  -> método pop
empty -> Vazia O(1) -> if not lista, len(lista)==0

"""
import operator
from typing import List


class ExpressaoInvalida(Exception):
    pass


def avaliar_notacao_polonesa_reversa(expressao: List[str]) -> int:
    """
    >>> avaliar_notacao_polonesa_reversa(["2", "1", "+", "3", "*"])
    9
    >>> avaliar_notacao_polonesa_reversa(["4", "13", "5", "/", "+"])
    6
    >>> avaliar_notacao_polonesa_reversa(["4", "13", "5", "/"])
    Traceback (most recent call last):
    ...
    ex_02_notacao_polonesa_reversa.ExpressaoInvalida: Sobrando operandos na expressão: ['4', '13', '5', '/']
    >>> avaliar_notacao_polonesa_reversa(["4", "13", "5", "/", '+', '-'])
    Traceback (most recent call last):
    ...
    ex_02_notacao_polonesa_reversa.ExpressaoInvalida: Faltando operandos na expressão: ['4', '13', '5', '/', '+', '-']
    >>> avaliar_notacao_polonesa_reversa(["4", "13", "5", '1', "/", "+", '-'])
    -14

    Seja n o tamanho dos elementos da expressão
    Seja m o número de operadores

    Análise de tempo de execução
    O(n * m )
    O(n) utilizando dicionário para operandos


    Análise de memória, pior caso:
    O(n/2 + 1) -> O(n/2) -> O(n)


    :param expressao:
    :return:
    """
    pilha = []

    operador_para_funcao = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
    }

    for operando_ou_operador in expressao:
        try:
            operando = int(operando_ou_operador)
            pilha.append(operando)
        except ValueError:
            operador = operando_ou_operador
            try:
                operando_2 = pilha.pop()
            except IndexError:
                raise ExpressaoInvalida(f'Faltando operandos na expressão: {expressao}')
            try:
                operando_1 = pilha.pop()
            except IndexError:
                raise ExpressaoInvalida(f'Faltando operandos na expressão: {expressao}')

            funcao = operador_para_funcao[operador]
            resultado = funcao(operando_1, operando_2)

            pilha.append(resultado)

    if len(pilha) > 1:
        raise ExpressaoInvalida(f'Sobrando operandos na expressão: {expressao}')
    return pilha.pop()
