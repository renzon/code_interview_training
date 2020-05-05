from functools import wraps
from time import strftime


def logar_datahora(talvez_funcao = None, *, formato='%H:%M:%S'):
    if talvez_funcao is not None:
        return logar_datahora(formato=formato)(talvez_funcao)

    def decoradora(funcao):
        @wraps(funcao)
        def envoltoria(*arg, **kwargs):
            print(strftime(formato))
            return funcao(*arg, **kwargs)

        return envoltoria

    return decoradora


# class logar_datahora:
#     def __init__(self, *, formato) -> None:
#         self.formato = formato

#     def __call__(self, funcao):
#         @wraps(funcao)
#         def envoltoria(*arg, **kwargs):
#             print(strftime(self.formato))
#             return funcao(*arg, **kwargs)

#         return envoltoria

    

@logar_datahora(formato='%Y/%d/%m %H:%M:%S')
def soma(a, b):
    """
    Funçao soma
    """
    return a+b

# soma = logar_datahora(formato='%H:%M:%S')(soma)

@logar_datahora
def multiplicar(a, b):
    """
    Funçao multiplicar
    """
    return a*b


print(soma(1,2))
print(soma(2,3))
# print(soma.__doc__)
# print(soma.__name__)
print(multiplicar(2, 3))