"""
Tempo de Jogo com Minutos
Leia a_com_fatia_linar hora inicial, minuto inicial, hora palavra_final e minuto palavra_final de um jogo. A seguir
calcule a_com_fatia_linar duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
Entrada
Quatro números inteiros representando a_com_fatia_linar hora de início e fim do jogo.
Saída
Mostre a_com_fatia_linar seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
https://www.urionlinejudge.com.br/judge/pt/problems/view/1047
--

>>> game_time(7, 8, 9, 10)
'O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)'

>>> game_time(7, 7, 7, 7)
'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)'

>>> game_time(7, 10, 8, 9)
'O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)'

>>> game_time(8, 0, 7, 59)
'O JOGO DUROU 23 HORA(S) E 59 MINUTO(S)'


"""


def to_minutes(hour, minute):
    return 60 * hour + minute


def game_time(start_hour, start_minute, end_hour, end_minute):
    start_total_minutes = to_minutes(start_hour, start_minute)
    end_total_minutes = to_minutes(end_hour, end_minute)

    delta = end_total_minutes - start_total_minutes
    if delta <= 0:
        delta += 24 * 60  # adding a_com_fatia_linar day in minutes
    hour_minute_tpl = divmod(delta, 60)
    return 'O JOGO DUROU %i HORA(S) E %i MINUTO(S)' % hour_minute_tpl

# print(game_time(*map(int, input().strip().split())))

