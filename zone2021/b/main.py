#!/usr/bin/env python3

def main():
    n, d, h = map(int, input().split())
    dh = [list(map(int,input().split())) for _ in range(n)]    

    ll = sorted(dh, key=lambda x:x[1], reverse = True) #多次元配列のソートx[]で列を指定

    a = ll[0][0]
    y = ll[0][1]

    flag = True
    h_max = 0

    for m in dh:
        a, y = m[0], m[1]

        h_max = max(h_max, ((d*y)-(a*h))/(d-a))
    
    print(h_max)

main()