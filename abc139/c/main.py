#!/usr/bin/env python3

def main():
    n = int(input())
    h = list(map(int, input().split())) 

    ans = 0

    for i in range(n-1):
        j = i
        tmp = 0
        while j < n-1:
            if h[j] >= h[j+1]:
                j += 1
                tmp += 1
            else:
                break
        ans = max(ans, tmp)

    print(ans)

main()