import datetime
import operator
from datetime import timedelta
from functools import reduce
from itertools import groupby, accumulate, chain


def group(data):
    data.sort(key=operator.itemgetter('motivo'))

    def calc_timedelta(dct):
        return dct['fim'] - dct['inicio']

    def sum_freq_and_timedelta(resultado, delta):
        resultado['quantidade'] += 1
        resultado['tempo'] += delta
        return resultado

    for k, g in groupby(data, key=operator.itemgetter('motivo')):
        start = {
            'motivo': k,
            'tempo': timedelta(0, 0, 0, 0, 0, 0, 0),
            'quantidade': 0
        }

        result = reduce(sum_freq_and_timedelta, map(calc_timedelta, g), start)
        result['tempo'] = str(result['tempo'])
        yield result


def test():
    data = [{'motivo': 'Mecanica',
             'inicio': datetime.datetime(2018, 6, 28, 14, 26, 3, 108553),
             'fim': datetime.datetime(2018, 6, 28, 15, 26, 3, 107554)},
            {'motivo': 'Mecanica',
             'inicio': datetime.datetime(2018, 6, 28, 14, 26, 7, 446634),
             'fim': datetime.datetime(2018, 6, 28, 15, 26, 7, 445632)},
            {'motivo': 'Eletrica',
             'inicio': datetime.datetime(2018, 6, 28, 14, 26, 11, 873525),
             'fim': datetime.datetime(2018, 6, 28, 15, 26, 11, 872520)},
            {'motivo': 'Mecanica',
             'inicio': datetime.datetime(2018, 6, 28, 14, 26, 17, 607448),
             'fim': datetime.datetime(2018, 6, 28, 15, 26, 17, 607448)},
            {'motivo': 'Energia  Gs',
             'inicio': datetime.datetime(2018, 6, 28, 14, 26, 22, 655489),
             'fim': datetime.datetime(2018, 6, 28, 15, 26, 22, 655489)}]

    esperado = [
        {'motivo': 'Eletrica', 'tempo': '0:59:59.998995', 'quantidade': 1},
        {'motivo': 'Energia  Gs', 'tempo': '1:00:00', 'quantidade': 1},
        {'motivo': 'Mecanica',
         'tempo': '2:59:59.997999',
         'quantidade': 3},

    ]

    assert esperado == list(group(data))
