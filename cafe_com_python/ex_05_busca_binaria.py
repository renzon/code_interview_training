"""
max([1, 4, 2, 5])        O(n)
min([1, 4, 2, 5])        O(n)
mediana([1, 4, 2, 5])    O(n log(n))
busca([1, 4, 2, 5])      O(n)


max([1, 2, 4, 5])        O(1)
min([1, 2, 4, 5])        O(1)
mediana([1, 2, 4, 5])    O(1)
busca([1, 2, 4, 5])      O(lg(n))

[0, 200]  100
[0, 99]  50
[0, 49]  25
[26, 49] 37
[38, 49] 43
[38, 42] 40
[38, 39] 38

a(0) = n
a(1) = n / 2
a(2) = n / 4
a(2) = n / 8
...
...
a(i) = n / 2 ** i

1024
2048
4096

a(i) <= 1

<=>

n / 2 ** i <= 1

=>

lg(n / 2 ** i) =< lg(1)   =>

lg(n) - lg(2 ** i) =< 0  =>

lg(n) <=  i

"""


def bissecao_alta(lista_ordenada: list, elemento_a_ser_inserido: int):
    """
    >>> bissecao_alta([], -1)
    0
    >>> bissecao_alta([-1], 1)
    1
    >>> bissecao_alta([-1, 1], 2)
    2
    >>> bissecao_alta([-1, 1], -2)
    0
    >>> bissecao_alta([-1, 1], 0)
    1
    >>> bissecao_alta([-1, 1, 2], 0)
    1
    >>> bissecao_alta([-1, 1, 2], -2)
    0
    >>> bissecao_alta([-1, 1, 2], 1)
    2
    >>> bissecao_alta([-1, 1, 2], 3)
    3


    :param lista_ordenada:
    :param elemento_a_ser_inserido:
    :return:
    """
    indice_inicial = 0
    indice_final = len(lista_ordenada) - 1
    return _bissecao_alta_recursiva(lista_ordenada, elemento_a_ser_inserido, indice_inicial, indice_final)


def _bissecao_alta_recursiva(lista_ordenada: list, elemento_a_ser_inserido: int, indice_inicial: int,
                             indice_final: int):
    if indice_final < indice_inicial:
        return indice_inicial
    indice_do_meio = (indice_final + indice_inicial) // 2
    elemento_do_meio = lista_ordenada[indice_do_meio]

    if elemento_a_ser_inserido < elemento_do_meio:  # elimina metade superior
        indice_final = indice_do_meio - 1
    else:  # elimina metade inferior
        indice_inicial = indice_do_meio + 1

    return _bissecao_alta_recursiva(lista_ordenada, elemento_a_ser_inserido, indice_inicial, indice_final)


def bissecao_baixa(lista_ordenada: list, elemento_a_ser_inserido: int):
    """
    >>> bissecao_baixa([], -1)
    0
    >>> bissecao_baixa([-1], 1)
    1
    >>> bissecao_baixa([-1, 1], 2)
    2
    >>> bissecao_baixa([-1, 1], -2)
    0
    >>> bissecao_baixa([-1, 1], 0)
    1
    >>> bissecao_baixa([-1, 1, 2], 0)
    1
    >>> bissecao_baixa([-1, 1, 2], -2)
    0
    >>> bissecao_baixa([-1, 1, 2], 1)
    1
    >>> bissecao_baixa([-1, 1, 2], 3)
    3


    :param lista_ordenada:
    :param elemento_a_ser_inserido:
    :return:
    """
    indice_inicial = 0
    indice_final = len(lista_ordenada) - 1

    while indice_final >= indice_inicial:
        indice_do_meio = (indice_final + indice_inicial) // 2
        elemento_do_meio = lista_ordenada[indice_do_meio]

        if elemento_a_ser_inserido <= elemento_do_meio:  # elimina metade superior
            indice_final = indice_do_meio - 1
        else:  # elimina metade inferior
            indice_inicial = indice_do_meio + 1

    return indice_inicial
