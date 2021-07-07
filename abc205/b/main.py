#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    a = set(a)

    if len(a) == n:
        print('Yes')
    else:
        print('No')

main()