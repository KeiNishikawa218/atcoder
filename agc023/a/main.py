#!/usr/bin/env python3

def main():    
    from collections import Counter
    import math

    n = int(input())
    a = list(map(int, input().split())) 

    s = [0] + [0]*n

    for i in range(1, n+1):
        s[i] = s[i-1] + a[i-1]


    c = Counter(s)

    ans = 0
    
    for v in c.values():
        if v > 1:
            ans += v*(v-1)//2

    print(ans)
main()