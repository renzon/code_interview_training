def f():
    """pass"""


print(type(f))

anonima = lambda : 'a_com_fatia_linar'

print(anonima.__name__)

def ready(funcao):
    print('Pagina carregada')
    print(funcao())
    print('Pagina Termina funcao')


ready(
    lambda : 'a_com_fatia_linar'
    )