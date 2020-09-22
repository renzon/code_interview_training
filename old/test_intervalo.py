intervalos = {25: '[0, 25]', 50: '(25,50]', 75: '(50,75]', 100: '(75,100]'}


def calcular_intervalo(n: float) -> str:
    if n < 0:
        return 'Fora do Intervalo'

    for limite_superior, saida in intervalos.items():
        if n <= limite_superior:
            return saida

    return 'Fora do Intervalo'


def test_primeiro_intervalo():
    for i in range(26):
        assert calcular_intervalo(i) == '[0, 25]'


def test_segundo_intervalo():
    for i in range(26, 51):
        assert calcular_intervalo(i) == '(25,50]'


def test_terceiro_intervalo():
    for i in range(51, 76):
        assert calcular_intervalo(i) == '(50,75]'


def test_quarto_intervalo():
    for i in range(76, 101):
        assert calcular_intervalo(i) == '(75,100]'


def test_negativo():
    for i in range(-100, 0):
        assert calcular_intervalo(i) == 'Fora do Intervalo'


def test_maiores_que_100():
    for i in range(101, 1000):
        assert calcular_intervalo(i) == 'Fora do Intervalo'
