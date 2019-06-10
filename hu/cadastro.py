"""
Utilizando o conceito de dicionários, faça uma ficha de cadastro de 4 funcionários utilizando a seguinte
estrutura:
Chave: Nome Dados: Idade, email, setor, salario
Inclua os funcionários:
Joao Pereira, 25, joao.pereira@hurb.com, marketing, 1950
Maria Silva, 23, maria.silva@hurb.com, comercial, 2300
Pedro Peixoto, 32, pedro.peixoto@hurb.com, operacao, 2625
Luiza Almeida, 28, luiza.almeida@hurb.com, atendimento, 2120
Faça um programa que retorna o nome, email e setor de todos os funcionários com mais de 25 anos.

"""
import unittest


def filtrar_maiores_de_25(colaboradores):
    resultado = []
    for nome, (idade, email, setor, *_) in colaboradores:
        if idade > 25:
            adicionar(email, nome, resultado, setor)
    return resultado


def adicionar(email, nome, resultado, setor):
    resultado.append((nome, email, setor))


class TesteColaborabores(unittest.TestCase):
    def test_filtragem_colabores(self) -> None:
        colaboradores = [
            ('Joao Pereira', [25, 'joao.pereira@hurb.com', 'marketing', 1950, 4, 8]),
            ('Maria Silva', [23, 'maria.silva@hurb.com', 'comercial', 2300]),
            ('Pedro Peixoto', [32, 'pedro.peixoto@hurb.com', 'operacao', 2625]),
            ('Pedro Peixoto', [32, 'pedro.peixoto@hurb.com', 'operacao', 2625]),
            ('Luiza Almeida', [28, 'luiza.almeida@hurb.com', 'atendimento', 2120]),
        ]

        resultado = filtrar_maiores_de_25(colaboradores)
        self.assertEqual(3, len(resultado))
        self.assertSetEqual(
            {
                ('Pedro Peixoto', 'pedro.peixoto@hurb.com', 'operacao'),
                ('Luiza Almeida', 'luiza.almeida@hurb.com', 'atendimento'),
            },
            set(resultado)
        )

    def test_filtragem_colabores(self) -> None:
        colaboradores = [
            ('Joao Pereira', [25, 'joao.pereira@hurb.com', 'marketing', 1950, 4, 8]),
            ('Maria Silva', [23, 'maria.silva@hurb.com', 'comercial', 2300]),
            ('Pedro Peixoto', [32, 'pedro.peixoto@hurb.com', 'operacao', 2625]),
            ('Luiza Almeida', [28, 'luiza.almeida@hurb.com', 'atendimento', 2120]),
        ]

        resultado = top_colaborador(colaboradores)
        self.assertEqual(('Pedro Peixoto', 2625), resultado)
