#!/usr/bin/env python3

def main():
    n, p = map(int, input().split())

    mod = 10**9 + 7

    ans = (p - 1) * pow(p - 2, n - 1, mod) % mod

    print(ans)

main()