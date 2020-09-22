
def log2(n):
    if n<=1:
        return 0
    return 1+log2(n//2)

for i in range(513):
    print(i, log2(i))