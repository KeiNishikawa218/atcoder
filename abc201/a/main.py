#!/usr/bin/env python3

def main():
    a = list(map(int, input().split())) 
    a.sort()

    if a[2]+a[0] == 2*a[1]:
        print('Yes')
    else:
        print('No')


main()