import datetime
import operator
from datetime import timedelta
from itertools import groupby


def group(data):
    data.sort(key=operator.itemgetter('motivo'))

    def calc_timedelta(dct):
        return dct['fim'] - dct['inicio']

    for k, g in groupby(data, key=operator.itemgetter('motivo')):
        g = list(g)
        yield {
            'motivo': k,
            'tempo': str(sum(map(calc_timedelta, g), timedelta(0, 0, 0, 0, 0, 0, 0))),
            'quantidade': len(g)
        }


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
