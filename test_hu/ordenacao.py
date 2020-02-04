frutas = ['abacaxi', 'mamão', 'caqui', 'limão', 'maça', 'banana', 'fruta do conde', 'pêra', 'pitaya', 'lixia']


def inverter(fruta: str) -> str:
    dct = {'ê': 'e'}
    segunda_letra = fruta[1]
    return dct.get(segunda_letra, segunda_letra)


print(sorted(frutas, key=inverter))
