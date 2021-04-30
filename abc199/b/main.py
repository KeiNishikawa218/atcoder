#!/usr/bin/env python3

def main():
    n = int(input())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 


    print(max(min(b)-max(a)+1, 0))
    exit()
    ll = [1]*1000

    for i in range(a[0]-1, b[0]):
        ll[i] = 0

    for i in range(1, n):
        kk = [1]*1000
        for j in range(a[i]-1, b[i]):
            kk[j] = 0

        for m in range(1000):
            if ll[m] == kk[m] == 0:
                ll[m] = 0
            else:
                ll[m] = 1

    
    print(1000-sum(ll))
main()