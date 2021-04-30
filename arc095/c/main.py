#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    b = sorted(a)  

    m1 = b[n//2-1]
    m2 = b[n//2]

    for i in a:
        if m1 == m2:
            print(m1)
        elif i <= m1:
            print(m2)
        elif i >= m2:
            print(m1)
main()