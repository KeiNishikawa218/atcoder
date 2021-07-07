#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    sum_a = 0
    wk = 0
    max_a = -1

    for i in range(n):
        max_a = max(max_a, a[i])
        sum_a += a[i]
        wk += sum_a
        print((i+1)*max_a + wk)

main()