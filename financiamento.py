def calcular_saldo_devedor(saldo_anterior: float, parcela: float, juros: float) -> float:
    saldo_atual = saldo_anterior * (1 + juros) - parcela
    return saldo_atual


def calcular_tempo_financiamente_parcela_fixa(saldo_inicial: float, parcela: float, juros: float):
    print(f'Saldo Inicial: {saldo_inicial}')
    saldo_anterior = saldo_inicial
    total_pago = 0
    n_parcelas = 0
    while saldo_anterior > 0:
        saldo = calcular_saldo_devedor(saldo_anterior, parcela, juros)
        if saldo <= 0:
            parcela = parcela + saldo
            saldo = 0
        print(f'Parcela: {parcela:.2f}, Saldo Devedor:{saldo:.2f} ')
        saldo_anterior = saldo
        total_pago += parcela
        n_parcelas += 1
    print(f'Total Pago: {total_pago:.2f} - Juros Total: {(total_pago - saldo_inicial):.2f} - Parcelas: {n_parcelas}')


def sac(saldo_inicial: float, n_parcelas: int, juros: float):
    print(f'Saldo Inicial: {saldo_inicial}')
    amortizacao = saldo_inicial / n_parcelas
    saldo_atual = saldo_inicial
    total_pago = 0
    for _ in range(n_parcelas):
        parcela = amortizacao + juros * saldo_atual
        total_pago += parcela
        saldo_atual = calcular_saldo_devedor(saldo_atual, parcela, juros)
        print(f'Parcela: {parcela:.2f}, Saldo Devedor:{saldo_atual:.2f} ')
    print(f'Total Pago: {total_pago:.2f} - Juros Total: {(total_pago - saldo_inicial):.2f} - Parcelas: {n_parcelas}')


def calcular_tempo_financiamente_parcela_e_n_parcelas_fixas(saldo_inicial: float, n_parcelas: int, juros: float):
    parcela = 0.01
    while True:
        saldo = saldo_inicial
        for _ in range(n_parcelas):
            saldo = calcular_saldo_devedor(saldo, parcela, juros)
        if saldo <= 0:
            break
        else:
            parcela += 0.01
        # print(parcela, saldo)
    calcular_tempo_financiamente_parcela_fixa(saldo_inicial, parcela, juros)


if __name__ == '__main__':
    print('Parcela Fixa de 20')
    calcular_tempo_financiamente_parcela_fixa(50, 20, 0.05)
    print()
    print('Numero de Parcelas fixa em 3 e parcelas iguais')
    calcular_tempo_financiamente_parcela_e_n_parcelas_fixas(50, 6, 0.05)
    print()
    print('Numero de Parcelas fixa em 3 Tabela sac')
    sac(50, 6, 0.05)
