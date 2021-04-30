#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    even = 0
    m4 = 0
    m2 = 0

    for i in a:
        if i%2 == 1:
            even += 1
        elif i%4 == 0:
            m4 += 1
        else:
            m2 += 1

    if m2%2 == 0:
        if even - m4 > 1:
            print('No')
        else:
            print('Yes')
    else:
        even += 1
        if even - m4 > 1:
            print('No')
        else:
            print('Yes')
main()