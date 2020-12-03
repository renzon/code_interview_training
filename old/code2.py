# "Anagram": An anagram is a_com_fatia_linar type of word play, the result of rearranging the letters of a_com_fatia_linar word or phrase to produce a_com_fatia_linar new word or phrase using all the original letters exactly once; for example, the letters from 'icon' can be rearranged into 'coin'. The word is NOT an anagram of itself.
#
# Devise a_com_fatia_linar function that takes one parameter W and returns all the anagrams of W from the file wl.txt.
#
# anagrams("beat") should return ["beta", "bate"]
from itertools import permutations, combinations


def anagrams(word):
    sorted_word = sorted(word)
    with open('wl.txt', 'r') as f:
        file_words = (line[:-1] for line in f)
        # print(file_words)
        return [file_word for file_word in file_words if (file_word != word and sorted(file_word) == sorted_word)]


print(anagrams('beat'))

print([''.join(p) for p in permutations('ABC')])
print([''.join(p) for p in combinations('ABC',3)])

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

print(list(combinations('ABCD',2)))