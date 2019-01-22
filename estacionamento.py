"""
>>> estaciomento = Estacionamento(n_andares=3, n_vagas_por_andar=10)
>>> estaciomento.estacionar(Carro())
(0, 0)
>>> estaciomento.estacionar(Carro())
(0, 1)
>>> estaciomento.estacionar(Carro())
(0, 2)
>>> estaciomento.estacionar(Carro())
(0, 3)
>>> estaciomento.estacionar(Carro())
(0, 4)
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


class Carro:
    pass


class EstaciomentoCheio(Exception):
    pass


class Estacionamento:
    def __init__(self, n_andares=3, n_vagas_por_andar=10):
        self.n_vagas_por_andar = n_vagas_por_andar  # 10
        self.n_andares = n_andares  # 3
        self._ultima_vaga_ocupada = -1  # 0

    def estacionar(self, carro):
        self._ultima_vaga_ocupada += 1
        andar = self._ultima_vaga_ocupada // self.n_vagas_por_andar
        if andar > self.n_andares:
            raise EstaciomentoCheio()
        return andar, self._ultima_vaga_ocupada % self.n_vagas_por_andar  # andar =0
