#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())

    import math

    ans = 1

    for i in range(1, b-a+1):
        if math.floor(b/i) - math.ceil(a/i) > 0:
            ans = i

    print(ans)

    
main()