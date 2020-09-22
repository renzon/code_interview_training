"""
Ano Bissexto

Este problema foi utilizado em 469 Dojo(s).

A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.
Exemplos:

São bissextos por exemplo:

>>> ano_eh_bissexto(1600)
True
>>> ano_eh_bissexto(1732)
True
>>> ano_eh_bissexto(1888)
True
>>> ano_eh_bissexto(1944)
True
>>> ano_eh_bissexto(2008)
True

Não são bissextos por exemplo:

>>> ano_eh_bissexto(1742)
False
>>> ano_eh_bissexto(1889)
False
>>> ano_eh_bissexto(1951)
False
>>> ano_eh_bissexto(2011)
False

Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""


def ano_eh_bissexto(ano: int):
    ano = int(ano)
    return (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)
