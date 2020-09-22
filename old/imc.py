def calcular_imc(peso, altura):
    limites_superiores={
        17:"Muito abaixo do peso",
        18.5:"Abaixo do peso",
        25:"Peso normal",
        30:"Acima do peso",
        35:"Obesidade I",
        40: "Obesidade II (severa)",

    }
    imc = float(peso / (altura ** 2))
    for limite_superior, msg in limites_superiores.items():
        if imc < limite_superior:
            print(msg)
            break
    else:
        print("Obesidade III (mórbida)")
    return imc


try:
    print("Progama para caulcular IMC (Indice de Massa Corporal: )")

    nome = str(input("digite seu nome: "))
    peso = float(input("digite seu peso: "))
    altura = float(input("sua sua altura: "))
    idade = int(input("digite sua idade: "))

    imc=calcular_imc(peso, altura)
    print(f'Oi {nome} baseando se no seu peso de {peso}kg e na sua altura de  {altura}m seu IMC é {imc:.2f} sua idade de {idade}anos voce esta no:')



except:
    print("Error")