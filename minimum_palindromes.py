# http://codercareer.blogspot.com.br/2013/02/no-43-minimal-number-of-splits-on-string.html
def min_palindrome_split(word):
    if word == ''.join(reversed(word)):
        return 0
    return 1 + min(min_palindrome_split(word[:i]) + min_palindrome_split(word[i:])
                   for i in range(1, len(word)))

print(min_palindrome_split(''))
print(min_palindrome_split('a'))
print(min_palindrome_split('aa'))
print(min_palindrome_split('ab'))
print(min_palindrome_split('aba'))
print(min_palindrome_split('abaac'))