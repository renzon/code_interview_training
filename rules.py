# coding: UTF-8
from __future__ import absolute_import

import pytest

_rules = []


def exec_rules(n):
    classifier = []
    for rule in _rules:
        rule(n, classifier)
    return classifier


def rule(f):
    _rules.append(f)


@rule
def div_by_2(n, classifier):
    if n % 2 == 0:
        classifier.append('Divisible by 2')
    else:
        raise Exception('Not divisible by 2')


@rule
def div_by_3(n, classifier):
    if n % 3 == 0:
        classifier.append('Divisible by 3')
    else:
        raise Exception('Not divisible by 3')


@pytest.mark.parametrize('n', [6, 12, 18])
def test_divisible(n):
    assert exec_rules(n) == ['Divisible by 2', 'Divisible by 3']


@pytest.mark.parametrize('n', range(1, 6))
def test_not_divisible(n):
    with pytest.raises(Exception):
        exec_rules(n)
