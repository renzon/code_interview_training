def _hanoi_rec(n, origin, destination, aux):
    if n <= 1:
        print_movement(origin, destination)
    else:
        _hanoi_rec(n - 1, origin, aux, destination)
        print_movement(origin, destination)
        _hanoi_rec(n - 1, aux, destination, origin)


def print_movement(origin, destination):
    print('Move piece %s to %s' % (origin, destination))


def hanoi(n):
    _hanoi_rec(n, 'A', 'B', 'C')


for i in range(1, 10):
    print('###### Hanoi %s #####$$' % i)
    hanoi(i)
