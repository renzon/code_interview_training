"""
    >>> estacionamento = Estacionamento()
    >>> estacionamento.estacionar(Carro())
    (0, 0)
    >>> estacionamento.estacionar(Carro())
    (0, 1)
    >>> estacionamento.estacionar(Carro())
    (0, 2)
    >>> estacionamento.estacionar(Carro())
    (0, 3)
    >>> estacionamento.estacionar(Carro())
    (0, 4)
    >>> estacionamento.estacionar(Carro())
    (0, 5)
    >>> estacionamento.estacionar(Carro())
    (0, 6)
    >>> estacionamento.estacionar(Carro())
    (0, 7)
    >>> estacionamento.estacionar(Carro())
    (0, 8)
    >>> estacionamento.estacionar(Carro())
    (0, 9)
    >>> estacionamento.estacionar(Carro())
    (1, 0)
    >>> estacionamento.estacionar(Carro())
    (1, 1)
"""


class Estacionamento:
    ANDARES = 3
    VAGAS_POR_ANDAR = 10
    TOTAL_VAGAS = ANDARES * VAGAS_POR_ANDAR

    def __init__(self):
        self.ultima_posicao_ocupada = -1

    def estacionar(self, carro):
        self.ultima_posicao_ocupada += 1
        andar = self.ultima_posicao_ocupada // self.VAGAS_POR_ANDAR
        vaga_no_andar = self.ultima_posicao_ocupada % self.VAGAS_POR_ANDAR
        return andar, vaga_no_andar


class Carro:
    pass
