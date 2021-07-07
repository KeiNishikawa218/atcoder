#!/usr/bin/env python3

def main():
    from collections import deque
    n = int(input())
    r, g, b = [], [], []

    lr, lg, lb = len(r), len(g), len(b)

    for _ in range(n*2):
        ac = list(input().split())

        if ac[1] == 'R':
            r.append(int(ac[0]))
        elif ac[1] == 'B':
            b.append(int(ac[0]))
        else:
            g.append(int(ac[0]))

    if len(r)%2 == 0 and len(b)%2 == 0 and len(g)%2 == 0:
        print(0)
    else:
        even = deque()
        odd1 = deque()
        odd2 = deque()

        if lr%2 == 0:
            even.append(r)
            odd1.append(b)
            odd2.append(g)
        elif lg%2 == 0:
            even.append(g)
            odd1.append(r)
            odd2.append(b)
        else:
            even.append(b)
            odd1.append(r)
            odd2.append(g)          


main()