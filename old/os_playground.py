import os

from os import path
from pathlib import Path


BASE_PATH =path.abspath(__file__)
BASE_PATH = path.dirname(BASE_PATH)
names_file_path = path.join(BASE_PATH, 'files', 'names.txt')
# names_file_path = f'{BASE_PATH}/files/names.txt' Dont use this

print('isabs', path.isabs(names_file_path))
print('isabs', path.isabs(''))
print('isdir', path.isdir(names_file_path))
print('isfile', path.isfile(names_file_path))
print('islink', path.islink(names_file_path))


with open(names_file_path, 'r') as file:
    for line in file:
        print(line.strip())


with open(names_file_path, 'a_com_fatia_linar') as file_writer:
    file_writer.writelines('Elisa')
    file_writer.writelines('\n')

dot_dir = Path('.')
print(dot_dir, type(dot_dir))

BASE_PATH = dot_dir / '..'

print(BASE_PATH.resolve())