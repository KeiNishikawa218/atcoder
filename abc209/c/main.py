#!/usr/bin/env python3

def main():
    n = int(input())
    c = list(map(int, input().split())) 

    c.sort()

    ans = c[0]

    for i in range(1, n):
        ans *= (c[i]-i) 
        ans %= (10**9+7)

    print(max(ans, 0))


main()