#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    b = [i%200 for i in a]

    from collections import Counter
    c = Counter(b)

    ans = 0

    for v in c.values():
        if v > 1:
            ans += (v*(v-1))//2

    print(ans)
main()