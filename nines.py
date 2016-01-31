def nines(digits):
    n = 0
    for i in range(digits):
        n = n * 10 + 9
    return n

print(nines(5000))
