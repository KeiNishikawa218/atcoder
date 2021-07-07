#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())

    if a <= b and b/a <= 6:
        print('Yes')
    else:
        print('No')


main()