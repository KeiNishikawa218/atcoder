#!/usr/bin/env python3

def main():
    from itertools import permutations, combinations,combinations_with_replacement,product
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]

    a = [i for i in range(1, n)]
    p = list(permutations(a))
    
    cnt = 0

    for ll in p:
        ll = [0] + list(ll) + [0]
        tmp = 0
        for i in range(n):
            tmp += t[ll[i]][ll[i+1]]

        if tmp == k:
            cnt += 1

    print(cnt)


main()