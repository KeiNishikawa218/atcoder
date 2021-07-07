#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split())) 

    ll = [[i, a[i], k//n] for i in range(n)]

    ll = sorted(ll, key=lambda x:x[1]) #多次元配列のソートx[]で列を指定
    
    for i in range(k%n):
        ll[i][2] += 1
    
    ll = sorted(ll, key=lambda x:x[0]) #多次元配列のソートx[]で列を指定

    for l in ll:
        print(l[2])
main()