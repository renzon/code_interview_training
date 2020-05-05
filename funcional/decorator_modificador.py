from time import time
from functools import wraps

def envolver(funcao_envolvida):
    def editar_metadados(funcao_envoltoria):
        funcao_envoltoria.__name__ = funcao_envolvida.__name__
        funcao_envoltoria.__doc__ =  funcao_envolvida.__doc__
        return funcao_envoltoria

    return editar_metadados

def modicar(funcao):
    print('Trocar fqunção original por outra')

    @wraps(funcao)
    def funcao_envoltoria(*arg, **kwargs):
        """
        Funcao envoltaria
        """
        tempo_inicial=time()
        resultado = funcao(*arg, **kwargs)
        tempo_final = time()
        print(tempo_final - tempo_inicial)
        return resultado

    # envolver(funcao)
    # editar_metadados

    return funcao_envoltoria


@modicar
def soma(a, b):
    """
    Funçao soma
    """
    return a+b

print(soma(1, 2))
print(soma(1000000000, 2**10000))
print(soma.__name__)
help(soma)