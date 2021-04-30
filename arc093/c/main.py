#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    a = [0] + a + [0]
    
    ss = 0

    for i in range(n+1):
        ss += abs(a[i] - a[i+1])

    for i in range(1, n+1):
        print(ss - (abs(a[i]-a[i-1]) + abs(a[i]-a[i+1]) ) + abs(a[i-1]-a[i+1]))

main()