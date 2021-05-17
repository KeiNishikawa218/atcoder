#!/usr/bin/env python3

def main():
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))     

    b = [0]*k

    for i in range(k):
        b[i] = round(m/n*(a[i]))

    if sum(b) != m:
        b[0] += 1
        
    print(*b)
main()