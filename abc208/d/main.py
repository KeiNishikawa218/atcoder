#!/usr/bin/env python3

ans = 0

import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
g = [[] for i in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a-1].append([b-1, c])

print(g)

def dfs(v):
    global ans
    if temp[v]: return
    temp[v] = True
    for vv in g[v]:
        ans += vv[1]
        dfs(vv[0])

for i in range(n):
    temp = [False]*n

    dfs(i)
    print(temp)

print(ans)