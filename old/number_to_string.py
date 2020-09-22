# http://codercareer.blogspot.com.br/2014/09/no-55-translating-numbers-to-string.html


def translate_count(number):
    number_str = str(number)
    if number_str == '':
        return 0
    if len(number_str) == 1:
        return 1
    if len(number_str) == 2:
        return 2 if int(number) <= 26 else 1
    first_2_chars_count = translate_count(number_str[:2])
    if number_str:
        if first_2_chars_count == 2:
            return translate_count(number_str[2:]) + translate_count(number_str[1:])
        return translate_count(number_str[1:])


print(translate_count(12258))