#!/usr/bin/env python3

def main():
    n = int(input())
    # abc = [list(map(int, input().split())) for _ in range(n)]
    a, b, c = [], [], []
    dp = [[0]*(n+1) for _ in range(3)]

    for i in range(n):
        x, y, z = map(int, input().split())
        a.append(x)
        b.append(y)
        c.append(z)

    abc = [a+[0]]+[b+[0]]+[c+[0]]

    dp[0][0] = max(b[0], c[0])
    dp[1][0] = max(a[0], c[0])
    dp[2][0] = max(b[0], a[0])

    for i in range(1, n+1):
        for j in range(3):
            dp[j][i] += max(dp[(j+1)%3][i-1], dp[(j+2)%3][i-1]) + abc[j][i]

    mm = 0
    for i in range(3):
        mm = max(mm, dp[i][-1])

    print(mm)
main()