#!/usr/bin/env python3

def main():
    import math
    n = int(input())

    ans = [0]*n
    root = int(math.sqrt(n))

    for x in range(1, root+1):
        for y in range(1, root+1):
            for z in range(1, root+1):
                num = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if num <= n:
                    ans[num-1] += 1

    for a in ans:
        print(a)

main()