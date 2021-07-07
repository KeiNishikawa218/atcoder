#!/usr/bin/env python3

def main():
    n = int(input())
    t = list(map(int, input().split())) 
    dp = [[10*16]*101]*101010

    dp[0][0] = 0

    for i in range(n):
        for j in range(101010):
            if dp[i][j] != 10*16:
                dp[i + 1][j + t[i]] = min(dp[i + 1][j + t[i]], dp[i][j]);
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + t[i])

    ans = 10*16

    for i in range(101010):
        ans = min(ans, max(i, dp[n][i]))

    print(ans)
main()