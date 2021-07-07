#!/usr/bin/env python3

def main():
    n = int(input())
    s = list(input())

    if s[0] != s[-1]:
        print(1)
        exit()

    for i in range(1, n-1):
        if s[i] != s[0] and s[i+1] != s[0]:
            print(2)
            exit()

    print(-1)
main()