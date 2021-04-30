#!/usr/bin/env python3

def main():
    s = list(input())

    if s == s[::-1]:
        print('Yes')
        exit()
        
    for i in range(10):
        s = ['0'] + s
        
        if s == s[::-1]:
            print('Yes')
            exit()
    print('No')

main()