# http://codercareer.blogspot.com.br/2014/10/no-57-integer-identical-to-index.html?_sm_au_=iQVZ6QHtsMVH5kvQ


def brute_search(items):
    for index, item in enumerate(items):
        if index == item:
            return item


def recursive_search(items, offset=0):
    n = len(items) # n = 1 offset = 3 items=[3]
    if n == 0:
        return None
    middle_index = n // 2 # middle_index = 0
    middle_element = items[middle_index]  # middle_element = 3
    if offset+middle_index==middle_element: # 3 == 3
        return middle_element

    if offset+middle_index < middle_element: # 4 < 5
        return recursive_search(items[:middle_index], offset)
    else:
        return recursive_search(items[middle_index + 1:], offset + middle_index + 1)

recursive_search([-3, -1, 1, 3, 5])


print(brute_search([-3, -1, 1, 3]))