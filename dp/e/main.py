#!/usr/bin/env python3

def main():
    n, w = map(int, input().split())
    wight = [0]
    value = [0]

    mm = 1000*n+1

    dp = [[10**18]*(mm) for _ in range(n+1)]

    dp[0][0] = 0

    for _ in range(n):
        a, b = map(int, input().split())
        wight.append(a)
        value.append(b)

    for i in range(1, n+1):
        for j in range(mm):
            if value[i] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j-value[i]]+wight[i], dp[i-1][j])
    
    ans = mm-1
    while dp[n][ans] > w:
        ans -= 1

    print(ans)
main()