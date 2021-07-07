#!/usr/bin/env python3

def main():
    n = int(input())
    t = list(map(int, input().split())) 

    ll = 10**5+1
    dp = [[0]*(ll) for _ in range(n+1)]

    t = [0] + t
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(ll):
            if j >= t[i] and dp[i-1][j-t[i]]:
                dp[i][j] = 1
            if dp[i-1][j]:
                dp[i][j] = 1

    s = sum(t)
    ans = 10**10
    
    for j in range(ll):
        if dp[n][j]:
            ans = min(ans, max(j, s-j))

    print(ans)
    #ケース３はSum(89, 35, 14) = 138

    #mean戦略はｘ
    #mean = sum(t)//2 + 1
    #[1, 1, 1, 99, 100]のような平均が引っ張られるリストに対応できない
    
    #線形探索もｘ
    #とびとびの値（ケース３）に対応できない
    # for k in range(n):
    #     a, b = t[k], t[:k] + t[k+1:]

    #     #焼くのにかかる時間    
    #     mm = max(a, sum(b))


    #     for i in range(n - 1):
    #         Sa, Sb = a, sum(b)

    #         j = 0
    #         while Sa < Sb and j < n-1:
    #             Sa += b[j]
    #             Sb -= b[j]
    #             j += 1

    #             mm = min(mm, max(Sa, Sb))

    #             print(f'{Sa} {Sb} {mm}')
            
    # print(mm)
    
main()