def f():
    """pass"""


print(type(f))

anonima = lambda : 'a'

print(anonima.__name__)

def ready(funcao):
    print('Pagina carregada')
    print(funcao())
    print('Pagina Termina funcao')


ready(
    lambda : 'a'
    )