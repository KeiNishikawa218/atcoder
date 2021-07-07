#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    from collections import Counter
    cnt = Counter(a)

    ans = 0

    for i in range(n):
        ans += cnt[b[c[i]-1]]

    print(ans)


main()