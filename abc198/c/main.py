#!/usr/bin/env python3

def main():
    # import decimal
    from decimal import Decimal

    r, x, y = map(Decimal, input().split())

    ans = 2
    v = (x**2 + y**2) ** Decimal(1/2)

    if v == r:
        print(1)
        exit()
    while v > 2*r:
        v -= r
        ans += 1

    print(ans)
main()