#!/usr/bin/env python3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split())) 
    k = [int(input()) for _ in range(q)]

    k2 = [[i, k[i], 0] for i in range(q)]
    k2.append([0,0,0])

    k2 = sorted(k2, key=lambda x:x[1]) #多次元配列のソートx[]で列を指定

    ll = sorted(k.copy())
    ans = [0]*(10**5+1)
    
    from collections import deque
    
    a = deque(a)
    k = deque(k)
    ll = deque(ll)

    p = 0

    i = 1
    while len(a) > 0:
        p = a.popleft() - p + 1

        if p >= k2[i][1]:
            k2[i][2] = p + k2[i][1] - k2[i-1][1]
            i += 1
        else:
            if len(a) > 0:
                p = a.popleft()
    
    print(k2)
main()