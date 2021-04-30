#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())

    if n == 1:
        if m == 1:
            print(1)
        if m == 2:
            print(0)
        if m >= 3:
            print(m-2)
    elif n == 2:
        if m == 1:
            print(0)
        if m == 2:
            print(0)
        if m >= 3:
            print(0)
    elif n >= 3:
        if m == 1:
            print(n-2)
        if m == 2:
            print(0)
        if m >= 3:
            print((n-2)*(m-2))

main()