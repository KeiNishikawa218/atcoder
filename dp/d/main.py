#!/usr/bin/env python3

def main():
    n, w = map(int, input().split())
    wight = []
    value = []

    dp = [[0]*(w+1) for _ in range(n)]

    for _ in range(n):
        a, b = map(int, input().split())
        wight.append(a)
        value.append(b)

    for i in range(wight[0]-1, w+1):
        dp[0][i] = value[0]
    
    for i in range(1, n):
        for j in range(w+1):
            if wight[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-wight[i]]+value[i], dp[i-1][j])

    print(dp[n-1][-1])
main()