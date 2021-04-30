#!/usr/bin/env python3

def main():
    n, c, k = map(int, input().split())
    t = [int(input()) for _ in range(n)]

    t.sort()

    bus = 0

    for i in range(n-1):
        
        res = 0
        j = i
        while j < c:
            if t[i+1] - t[i] > k:
                bus += 1
                
            if res >= c:
                bus += 1
                i = j
                break
            if t[j+1] - t[j] <= k:
                res += 1
            else:
                i = j
                break

    print(bus)

main()