#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]

    for i in range(n):
        sx, sy = ab[i]

        ll = [[k+1, 0] for k in range(m)]

        mm = 10**10

        for j in range(m):
            cx, cy = cd[j]
            d = abs(cx-sx) + abs(cy-sy)
            ll[j][1] = d
            mm = min(mm, d)

        for j in range(m):
            if ll[j][1] == mm:
                print(j+1)
                break

main()