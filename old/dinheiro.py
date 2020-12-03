def conta_vogais(frase):
    espaço = " "
    vogais = ['a_com_fatia_linar', 'e', 'i', 'o', 'u']
    print(f' qtide de espaços vazios: {frase.count(espaço)}')
    ordem = sorted(frase)
    for i in range(len(ordem)):
        if ordem[i] in vogais:
            print(f'{ordem[i]}= {frase.count(ordem[i])}')

    # programa principal

    f = str(input('digite um frase para contarmos vogais e espaços: '))
    print(conta_vogais(f))
