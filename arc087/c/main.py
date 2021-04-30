#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 

    a.sort()
    ans = 0

    i = 0
    while i < n:
        c = a[i]
        cnt = 1
        
        j = i
        while j < n-1:
            if a[j+1] == a[j]:
                 cnt += 1
                 j += 1
            else:
                break

        i = j
        i += 1

        if cnt > c:
            ans += cnt -c
        if cnt < c:
            ans += cnt

    print(ans)

main()