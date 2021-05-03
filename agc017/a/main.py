#!/usr/bin/env python3

def main():
    from scipy.special import comb
    n, p = map(int, input().split())
    a = list(map(int, input().split())) 

    e, o = 0, 0

    for i in a:
        if i%2 == 0:
            e += 1
        else:
            o += 1

    if n == e:
        if p == 0:
            print(2**n)
        else:
            print(0)
    else:
        print(2**(n-1))
main()