#!/usr/bin/env python3

def main():
    n = int(input())
    s = input()

    cnt = [0]*(n+1)

    for i in range(n):
        cnt[i+1] = cnt[i]
        if s[i] == 'W':
            cnt[i+1] += 1
    
    ans = n

    for i in range(1, n+1):
        ans = min(ans, cnt[i-1]+(n-i)-(cnt[n]-cnt[i]))

    print(ans)
main()