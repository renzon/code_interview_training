# http://codercareer.blogspot.com.br/2013/02/no-43-minimal-number-of-splits-on-string.html


def is_palindrome(word):
    return word == ''.join(reversed(word))


def min_palindrome_split(word):
    if is_palindrome(word):
        return 0
    substrings = ((word[:i], word[i:]) for i in range(1, len(word)))
    substrings_begin_is_palindrome = filter(lambda tpl: is_palindrome(tpl[0]), substrings)
    not_palindromes=map(lambda tpl: tpl[1], substrings_begin_is_palindrome)
    return 1 + min(min_palindrome_split(end) for end in not_palindromes)


def min_palindrome_split2(word):
    if word == ''.join(reversed(word)):
        return 0
    return 1 + min(min_palindrome_split(word[:i]) + min_palindrome_split(word[i:])
                   for i in range(1, len(word)))


print(min_palindrome_split(''))
print(min_palindrome_split2(''))
print(min_palindrome_split('a'))
print(min_palindrome_split2('a'))
print(min_palindrome_split('aa'))
print(min_palindrome_split2('aa'))
print(min_palindrome_split('ab'))
print(min_palindrome_split2('ab'))
print(min_palindrome_split('aba'))
print(min_palindrome_split2('aba'))
print(min_palindrome_split('abaac'))
print(min_palindrome_split2('abaac'))
