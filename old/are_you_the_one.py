from random import shuffle

_ = list('ABCDEFGHIJ')
shuffle(_)
perfect_women_order = ''.join(_)


def match(women_sample):
    return sum(1 if p == w else 0 for p, w in zip(perfect_women_order, women_sample))


def perfect(man, woman):
    return perfect_women_order[man] == woman
