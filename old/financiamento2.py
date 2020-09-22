saldo_devedor = 100_000.00
total = 0
n_parcelas = 360
juros = 0.0062

saldo = saldo_devedor
amortizacao = saldo_devedor / n_parcelas

for i in range(n_parcelas):
    parcela = amortizacao + juros * saldo
    total +=parcela
    saldo -= amortizacao
    print(f'Saldor Devedor: R$ {saldo:.2f} Parcela: R$ {parcela:.2f}')

percentual_total = (total - saldo_devedor) / saldo_devedor
print(
    f'Valor Financiamento: R$ {saldo_devedor:.2f}, Total R$ {total:.2f}, Percentual Total: {percentual_total:.2%}, '
    f'Parcelas: {n_parcelas}')
