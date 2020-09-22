class OperacaoNaoEncontrada(Exception):
    pass


class Soma:
    def __call__(self, operandos):
        return operandos[0] + operandos[1]


class Subtracao:
    def __call__(self, operandos):
        return operandos[0] - operandos[1]


class Calculadora:

    def __init__(self):
        self.operacoes = {}
        self.adicionar_operacao('+', Soma())
        self.adicionar_operacao('-', Subtracao())

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao

    def calcular(self):

        operandos = []
        operandos.append(float(input('digite um numero: ')))
        sinal = input(('digite o sinal da operação: '))
        operandos.append(float(input('digite um numero: ')))
        try:
            operacao = self.operacoes[sinal]
            resultado = operacao(operandos)

        except KeyError as e:
            raise OperacaoNaoEncontrada('Operação nao encontrada!') from e
        return resultado


def s_or_no():
    while True:
        s_n=str(input("deseja continuar S/N ")).strip().upper()
        if s_n in {"N", "S"}:
            return s_n


if __name__ == '__main__':
    print('aqui')
    print(Calculadora().calcular())
