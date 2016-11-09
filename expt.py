def expt(base, n):
    def linear(base, n, result=1):
        if n == 0:
            return result
        return linear(base, n - 1, result * base)

    return linear(base, n)

# b^(2n) = (b^2)ˆn
def expt_fast(base, n):
    def logarithmic(base, n, result=1):
        if n == 0:
            return result
        if n % 2 == 0:
            return logarithmic(base * base, n / 2, result)
        return logarithmic(base, n - 1, result * base)

    return logarithmic(base, n)


for i in range(11):
    print(expt(2, i), expt_fast(2,i))
