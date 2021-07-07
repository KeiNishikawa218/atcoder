#!/usr/bin/env python3

def main():
    n = int(input())

    a, b = [0]*n, [0]*n

    for i in range(n):
        t, l, r = map(int, input().split())

        if t == 1:
            a[i], b[i] = l*2, r*2+1
        elif t == 2:
            a[i], b[i] = l*2, r*2
        elif t == 3:
            a[i], b[i] = l*2+1, r*2+1
        else:
            a[i], b[i] = l*2+1, r*2

    ans = 0

    for i in range(n):
        for j in range(i+1, n):
            aa = max(a[i], a[j])
            bb = min(b[i], b[j])
            if aa < bb:
                ans += 1

    print(ans)
main()