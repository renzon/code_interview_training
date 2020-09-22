from itertools import permutations, product


def merge_perms(set_1, comb_1, set_2, comb_2):
    perms_1 = permutations(set_1, comb_1)
    perms_2 = permutations(set_2, comb_2)
    perms_product = product(perms_1, perms_2)
    for perm_1, perm_2 in perms_product:
        yield perm_1 + perm_2


print(list(merge_perms(range(1, 6), 3, range(6, 9), 2)))
