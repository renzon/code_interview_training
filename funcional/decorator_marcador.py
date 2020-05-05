
_funcoes_marcadas = []

def marcar(funcao):
    _funcoes_marcadas.append(funcao)
    return funcao

@marcar
def f():
    pass

# f=marcar(f)

def g():
    pass

g = marcar(g)

print([f.__name__ for f in _funcoes_marcadas])
print(f)
print(g)

def positivo(b):
    return b


def oposto(b):
    return -b

def modulo(b):
    funcao = oposto
    if b > 0:
        funcao = positivo

    return funcao(b)

print(modulo(1))
print(modulo(-1))