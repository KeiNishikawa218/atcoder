#!/usr/bin/env python3

def main():
    n, a, b = map(int, input().split())

    if a == b:
        print(1)
    else:
        print(max(0, (b-a)*(n-2)+1))

main()