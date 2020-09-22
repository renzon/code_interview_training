# http://codercareer.blogspot.com.br/2013/02/no-38-digits-in-sequence.html
def sequence(i=0):
    for char in str(i):
        yield char
    yield from sequence(i + 1)


def find_digit(n):
    seq = sequence()
    for i in range(n):
        next(seq)
    return next(seq)


for i in range(14):
    print(find_digit(i))