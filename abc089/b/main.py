#!/usr/bin/env python3

def main():
    n = int(input())
    s = list(map(str, input().split())) 

    if 'Y' in s:
        print('Four')
    else:
        print('Three')


main()