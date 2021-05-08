#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    res1 = 0
    res2 = 0
    y = 0

    for i in a:
        res1 = i**2
        res2 = -2*i

    for i in range(min(a), max(a)+1):
        y = res1 + res2*i + n*i

        print(y)


main()