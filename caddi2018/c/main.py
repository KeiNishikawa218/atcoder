#!/usr/bin/env python3

def main():
    n, p = list(map(int, input().split())) 


    # n, p = 2, (2**4)*(3**4)
    pf={}
    m=p
    for i in range(2,int(m**0.5)+1):
        while m%i==0:
            pf[i]=pf.get(i,0)+1
            m//=i
    if m>1:pf[m]=1

    ans = 1

    for k, v in pf.items():
        if v >= n:
            ans *= k**(v//n)

    print(ans)

main()