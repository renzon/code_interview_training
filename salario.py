from unittest import TestCase


def formatar_real(salario: float):
    return f'R$ {salario:.2f}'


def calcular_ir(salario):
    pass


class TestSalario(TestCase):
    def test_formato_salario_alto(self):
        salario = 1234.79
        resultado = formatar_real(salario)
        esperado = 'R$ 1234.79'
        self.assertEqual(esperado, resultado)

    def test_formato_salario_baixo(self):
        salario = 234
        resultado = formatar_real(salario)
        esperado = 'R$ 234.00'
        self.assertEqual(esperado, resultado)

    def test_imposto_de_renda(self):
        salario = 100.00
        resultado = calcular_ir(salario)
        esperado = 'R$ 11.00'
        self.assertEqual(esperado, resultado)



