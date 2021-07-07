#!/usr/bin/env python3

def main():
    import math
    a, b, c, d = map(int, input().split())

    if c*d <= b:
        print(-1)
        exit()

    if c*d-b != 0:
        print(max(math.ceil(a/(c*d-b)), -1))

main()