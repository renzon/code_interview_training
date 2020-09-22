"""
>>> estaciomento = Estacionamento(n_andares=3, n_vagas_por_andar=10)
>>> estaciomento.estacionar(Moto())
(0, 0)
>>> estaciomento.estacionar(Moto())
(0, 0)
>>> estaciomento.estacionar(Moto())
(0, 1)
>>> estaciomento.estacionar(Carro())
(0, 2)
>>> estaciomento.estacionar(Carro())
(0, 3)
>>> estaciomento.estacionar(Carro())
(0, 4)
>>> estaciomento.estacionar(Moto())
(0, 1)
>>> estaciomento.estacionar(Carro())
(0, 5)
>>> estaciomento.estacionar(Carro())
(0, 6)
>>> estaciomento.estacionar(Carro())
(0, 7)
>>> estaciomento.estacionar(Carro())
(0, 8)
>>> estaciomento.estacionar(Carro())
(0, 9)
>>> estaciomento.estacionar(Carro())
(1, 0)

"""


class Moto:
    espacos_ocupados = 1


class Carro:
    espacos_ocupados = 2


class EstaciomentoCheio(Exception):
    pass


class VagaCheia(Exception):
    pass


class Vaga:
    def __init__(self):
        self._espacos_disponiveis = 2

    def estacionar(self, veiculo):
        if self._espacos_disponiveis < veiculo.espacos_ocupados:
            raise VagaCheia()
        self._espacos_disponiveis -= veiculo.espacos_ocupados


class AndarCheio(Exception):
    pass


class Andar:
    def __init__(self, n_vagas_por_andar):
        self._vagas = [Vaga() for _ in range(n_vagas_por_andar)]

    def estacionar(self, veiculo):
        for i, vaga in enumerate(self._vagas):  # i=1, vaga[0]= 0, vagas[1]=1
            try:
                vaga.estacionar(veiculo)
            except VagaCheia:
                pass  # logar vaga cheia
            else:
                return i
        raise AndarCheio()


class Estacionamento:
    def __init__(self, n_andares=3, n_vagas_por_andar=10):
        self._andares = [Andar(n_vagas_por_andar) for _ in range(n_andares)]

    def estacionar(self, veiculo):
        for i, andar in enumerate(self._andares):  # i=0, andar[0]
            try:
                return i, andar.estacionar(veiculo)
            except AndarCheio:
                pass  # logar andar cheio

        raise EstaciomentoCheio()
