from itertools import count


def numero_crescente(n: int) -> bool:
    n_str = str(n)
    anterior = 0
    for c in n_str:
        c = int(c)
        if anterior > c:
            return False
        anterior = c
    return True


def numero_decrescente(n: int) -> bool:
    n_str = ''.join(reversed(str(n)))
    return numero_crescente(int(n_str))


def is_bouncy(n: int) -> bool:
    return (not numero_crescente(n)) and (not numero_decrescente(n))


def bouncy_number(freq: float) -> int:
    bouncy_qtd = 0
    for i in count(100):
        if is_bouncy(i):
            bouncy_qtd += 1
            freq_calculado = bouncy_qtd / i
            if freq_calculado >= freq:
                return i


def test_verificar_numero_crescente():
    assert numero_crescente(134468)
    assert numero_crescente(12)
    assert numero_crescente(123)
    assert numero_crescente(1234)


def test_verificar_numero_nao_crescente():
    assert not numero_crescente(21)
    assert not numero_crescente(1231)
    assert not numero_crescente(12313)


def test_verificar_numero_descrescente():
    assert numero_decrescente(66420)
    assert numero_decrescente(21)
    assert numero_decrescente(321)
    assert numero_decrescente(3321)
    assert numero_decrescente(43321)


def test_verificar_numero_nao_decrescente():
    assert not numero_decrescente(12)
    assert not numero_decrescente(1231)
    assert not numero_decrescente(12313)


def test_bouncy():
    assert is_bouncy(155349)


def test_frequencia():
    assert bouncy_number(0.5) == 538
    assert bouncy_number(0.9) == 21780
    assert bouncy_number(0.99) == 1587000
