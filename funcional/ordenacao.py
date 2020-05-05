frutas = 'caqui jaca uva kiwI manga abacaxi jaboticaBA mangaba'.split()

def reverter(fruta:str):
    print(fruta)
    fruta_reversa=(fruta[::-1]).lower()
    print(fruta_reversa)
    return fruta_reversa


frutas.sort(key=reverter)
print(frutas)
