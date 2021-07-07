#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    s = (n-1)*(n)//2

    from collections import Counter

    c = Counter(a)

    m = 0

    for v in c.values():
        if v > 1:
            m += (v-1)*v//2
    print(s-m)

main()