#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 
    
    mod = pow(10, 9) + 7

    if n == 1:
        print(a[0])
        exit()

    x, y = 1, 1
    dp = [1, 1]

    for _ in range(n-2):
        dp.append(x+y)
        x, y = y%mod, x+y%mod
    
    print(dp)
    ans = sum(a)*(x+y)%mod

    for i in range(1, n):
        j = i - 1
        k = n - i - 1
        ans -= 2*a[i]*dp[j]*dp[k]
        ans %= mod

    print(ans)
main()