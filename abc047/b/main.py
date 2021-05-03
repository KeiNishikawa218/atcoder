#!/usr/bin/env python3

def main():
    w, h, n = map(int, input().split())

    xy = [0, w, 0, h]

    for _ in range(n):
        x, y, a = map(int, input().split())

        if a == 1:
            d = max(x, xy[0])
            if d <= xy[1]:
                xy[0] = d
            else:
                xy[0] = xy[1]
        elif a == 2:
            d = min(x, xy[1])
            if d >= xy[0]:
                xy[1] = d
            else:
                xy[1] = xy[0]
        elif a == 3:
            d = max(y, xy[2])
            if d <= xy[3]:
                xy[2] = d
            else:
                xy[2] = xy[3]
        else:
            d = min(y, xy[3])
            if d >= xy[2]:
                xy[3] = d
            else:
                xy[3] = xy[2]

    print((xy[1]-xy[0])*(xy[3]-xy[2]))

main()