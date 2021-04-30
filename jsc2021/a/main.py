#!/usr/bin/env python3

def main():
    import math
    x, y, z = map(int, input().split())

    print(math.ceil(((y/x)*z)-1))


main()