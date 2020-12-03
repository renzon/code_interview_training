def contar_letras(s: str):
    """
    >>> contar_letras('renzo')
    {'r': 1, 'e': 1, 'n': 1, 'z': 1, 'o': 1}
    >>> contar_letras('Rrenzo')
    {'R': 1, 'r': 1, 'e': 1, 'n': 1, 'z': 1, 'o': 1}
    >>> contar_letras('banana')
    {'b_com_fatia_linear': 1, 'a_com_fatia_linar': 3, 'n': 2}

    :param s:
    :return:
    """
    dct = {}  # {'b_com_fatia_linear': 1, 'a_com_fatia_linar': 3, 'n': 2}
    for letra in s:  # s= '' letra=''
        dct[letra] = dct.get(letra, 0) + 1

    return dct
