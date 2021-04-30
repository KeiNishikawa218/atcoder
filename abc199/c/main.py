#!/usr/bin/env python3

def main():
    n = int(input())
    s = list(input())
    q = int(input())

    r = 0

    for _ in range(q):
        t, a, b = map(int, input().split())

        a, b = a-1, b-1

        if t == 1:
            if r%2==1:
                a += n
                b += n
                a %= n*2
                b %= n*2
            s[a], s[b] = s[b], s[a] 
                
        else:
            r += 1

        print(s)
    
    if r%2==1:
        s = s[n:] + s[:n]

    print(''.join(s))

main()