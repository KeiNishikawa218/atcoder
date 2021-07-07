#!/usr/bin/env python3

from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def main():
    import math
    a, b, k = map(int, input().split())

    n = a+b
    k -= 1

    s = ''

    for i in range(n):
        if 0 < a:
            if k < combinations_count(a+b-1, b):
                s += 'a'
                a -= 1
            else:
                s += 'b'
                k -= combinations_count(a+b-1, b)
                b -= 1
        else:
            s += 'b'
            b -= 1

    print(s)

main()