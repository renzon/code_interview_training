
def calculate_harmonic_number(n):
    if n <=1:
        return 1
    return 1/n+calculate_harmonic_number(n-1)

for i in range(999):
    print(i, calculate_harmonic_number(i))