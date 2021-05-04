#!/usr/bin/env python3

def main():
    n = int(input())

    rem = n

    for i in range(n, 0, -1):
        if rem > i*(i-1)/2:
            print(i)
            rem -= i

main()