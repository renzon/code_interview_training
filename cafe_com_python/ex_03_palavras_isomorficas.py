"""
Enunciado: https://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/
"""


def sao_isomorficas(s: str, t: str) -> bool:
    """
    >>> sao_isomorficas('egg', 'foo')
    True
    >>> sao_isomorficas('egg', 'foe')
    False
    >>> sao_isomorficas('egg', 'ooo')
    True
    >>> sao_isomorficas('egg', 'fooo')
    False
    >>> sao_isomorficas('egge', 'foo')
    False
    >>> sao_isomorficas('egge', 'foox')
    False


    Análise de complexidade

    :param s:
    :param t:
    :return: boleano informando se t e s são (True) ou não (False) isomórficas

    O(n) para tempo de execução e memória

    """
    if len(s) != len(t):
        return False
    dct = {}

    for letra_em_s, letra_em_t in zip(s, t):
        try:
            valor_de_s_eh_respectivo_a_letra_de_t = (dct[letra_em_s] == letra_em_t)
        except KeyError:
            dct[letra_em_s] = letra_em_t
        else:
            if not valor_de_s_eh_respectivo_a_letra_de_t:
                return False

    return True
