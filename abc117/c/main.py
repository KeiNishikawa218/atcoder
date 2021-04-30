#!/usr/bin/env python3

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split())) 

    a.sort()

    b = [abs(a[i]-a[i+1]) for i in range(m-1)]

    b.sort(reverse=True)

    print(sum(b[n-1:]))

main()