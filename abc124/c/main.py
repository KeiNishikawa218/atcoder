#!/usr/bin/env python3

def main():
    s = list(input())
    t = s.copy()[::-1]

    ans1 = 0
    ans2 = 0

    for i in range(len(s)-1):
        n1 = int(s[i]) + int(s[i+1])
        n2 = int(t[i]) + int(t[i+1])
        
        if n1 != 1:
            if n1 == 0:
                s[i+1] = '1'
            else:
                s[i+1] = '0'
            ans1 += 1
        
        if n2 != 1:
            if n2 == 0:
                t[i+1] = '1'
            else:
                t[i+1] = '0'
            ans2 += 1

    print(min(ans1, ans2))
main()