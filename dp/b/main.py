#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split())) 

    dp = [0]*(n)

    for i in range(1, min(n, k)):
        dp[i] = abs(h[i]-h[0])

    for i in range(min(n, k), n):
        mm = 10**18
        for j in range(1, min(n, k+1)):
            mm = min(mm, abs(h[i]-h[i-j])+dp[i-j])

        dp[i] += mm
    print(dp[-1]) 


main()