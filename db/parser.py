def extract_value(s: str):
    value = s.split('=')[1]
    return value.strip()


def extract():
    database_name = None
    database_status = None
    with open('input.txt', mode='r', encoding='utf8') as f:
        for line in f:
            if database_name is None:
                database_name = extract_value(line)
            elif database_status is None:
                database_status = extract_value(line)
                yield database_name, database_status
            else:
                database_name = None
                database_status = None


if __name__ == '__main__':
    print(dict(extract()))
