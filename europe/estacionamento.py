"""
>>> # Resolvendo problema da Vaga
>>> vaga = Vaga()
>>> vaga.espacos_disponiveis
2
>>> vaga.estacionar(Moto())
>>> vaga.espacos_disponiveis
1
>>> vaga.estacionar(Moto())
>>> vaga.espacos_disponiveis
0
>>> vaga = Vaga()
>>> vaga.estacionar(Carro())
>>> vaga.espacos_disponiveis
0
>>> vaga = Vaga()
>>> vaga.estacionar(Moto())
>>> vaga.espacos_disponiveis
1
>>> vaga.estacionar(Carro())
Traceback (most recent call last):
...
estacionamento.VagaOverFlow: não há vagas
>>> vaga.espacos_disponiveis
1
>>> # Resolvendo problema do Andar
>>> andar = Andar()
>>> andar.estacionar(Moto())
0
>>> andar.estacionar(Moto())
0
>>> andar.estacionar(Moto())
1
>>> andar.estacionar(Carro())
2
>>> andar.estacionar(Carro())
3
>>> andar.estacionar(Carro())
4
>>> andar.estacionar(Carro())
5
>>> andar.estacionar(Carro())
6
>>> andar.estacionar(Moto())
1
>>> andar.estacionar(Carro())
7
>>> andar.estacionar(Carro())
8
>>> andar.estacionar(Carro())
9
>>> andar.estacionar(Carro())
Traceback (most recent call last):
...
estacionamento.VagaOverFlow: não há vagas




>>> estacionamento = Estacionamento()
>>> estacionamento.estacionar(Moto())
(0, 0)
>>> estacionamento.estacionar(Moto())
(0, 0)
>>> estacionamento.estacionar(Moto())
(0, 1)
>>> estacionamento.estacionar(Carro())
(0, 2)
>>> estacionamento.estacionar(Moto())
(0, 1)
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


class Veiculo:
    @property
    def espacos(self):
        raise NotImplementedError()


class Carro(Veiculo):
    @property
    def espacos(self):
        return 2


class Moto(Veiculo):
    @property
    def espacos(self):
        return 1


class Vaga:
    ESPACOS = 2

    def __init__(self):
        self.espacos_disponiveis = self.ESPACOS

    def estacionar(self, veiculo: Veiculo):
        if veiculo.espacos > self.espacos_disponiveis:
            raise VagaOverFlow('não há vagas')
        self.espacos_disponiveis -= veiculo.espacos


class Andar:
    VAGAS_POR_ANDAR = 10

    def __init__(self):
        self.vagas = [Vaga() for _ in range(self.VAGAS_POR_ANDAR)]

    def estacionar(self, veiculo: Veiculo):
        for i, vaga in enumerate(self.vagas):
            try:
                vaga.estacionar(veiculo)
            except VagaOverFlow:
                pass
            else:
                return i
        raise VagaOverFlow('não há vagas')


class VagaOverFlow(Exception):
    pass


class Estacionamento:
    ANDARES = 3

    def __init__(self):
        self.andares = [Andar() for _ in range(self.ANDARES)]

    def estacionar(self, veiculo):
        for i, andar in enumerate(self.andares):
            try:
                vaga = andar.estacionar(veiculo)
            except VagaOverFlow:
                pass
            else:
                return i, vaga
        raise VagaOverFlow('não há vagas')
