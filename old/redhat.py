count = 0


def pow_log(base, power):
    if base == 0 and power == 0:
        raise ValueError()

    def pow_rec(p):
        global count
        count += 1
        if p == 0:
            return 1
        elif p % 2 == 0:
            partial = pow_rec(p / 2)
            return partial * partial
        else:
            return base * pow_rec(p - 1)

    return pow_rec(power)


def pow(base, power):
    if base == 0 and power == 0:
        raise ValueError()

    def pow_rec(p, r=1):
        global count
        count += 1
        if p == 0:
            return r
        return pow_rec(p - 1, r * base)

    return pow_rec(power)


base = -2
power = 320
print(pow(base, power))
print(count)

count = 0

print(pow_log(base, power))
print(count)
