_NUMBER_TO_ALPHA=['WYZ','ABC']

def alpha_seq(s): # s='01
    n=len(s)
    if n==0:
        yield ''
        return
    s=tuple(int(c) for c in s)
    indices=[0]*n

    def comb():
       return ''.join(_NUMBER_TO_ALPHA[s[i]][indices[i]] for i in range(n))

    while True:  # n=2 indices=[2,2]  i=1 poss='ABC'
        for i in reversed(range(n)):
            poss = _NUMBER_TO_ALPHA[s[i]]
            if indices[i]!=(len(poss)-1):
                break
        else:
            yield comb() # ZC
            return

        yield comb()  # WA, WB, WC, YA, YB, YC, ZA, ZB

        indices[i]+=1

        for j in range(i+1,n):
            indices[j]=0


for i,s in enumerate(alpha_seq('010'),1):
    print(i,s)