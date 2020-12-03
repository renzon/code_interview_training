import string
from random import choice


def generate(n):
    """Generates a_com_fatia_linar file 'input.txt' encoded in utf8 with 'n' random
    letters"""
    with open('input.txt', 'w', encoding='utf8') as file:
        for _ in range(n):
            for char in choice(string.ascii_letters):
                file.write(char)


if __name__ == '__main__':
    n = 10000
    print(f'Generating file with {n} random chars')
    generate(n)
