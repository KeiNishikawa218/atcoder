#!/usr/bin/env python3

def main():
    import math
    t, n = map(int, input().split())

    print(n+math.ceil(n/t*100)-1)


main()