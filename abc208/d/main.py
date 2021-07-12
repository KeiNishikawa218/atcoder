#!/usr/bin/env python3

import sys

n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

d = [[1 << 60]*n for i in range(n)]

for i in range(n):
    d[i][i] = 0

for a, b, c in abc:
    d[a-1][b-1] = c

ans = 0

for k in range(n):
    nxt = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            nxt[i][j] = min(d[i][j], d[i][k]+d[k][j])
            if nxt[i][j] < 1 << 59:
                ans += nxt[i][j]

    d = nxt

print(ans)
