#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()

    ans = 0

    for i in range(k):
        flag = False

        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        else:
            ans += s
        
        for j in range(i, n-k, k):
            if t[j] != t[j+k]:
                if t[j+k] == 'r':
                    ans += p
                elif t[j+k] == 's':
                    ans += r
                else:
                    ans += s

                flag = False
            elif t[j] == t[j+k] and flag == False:
                flag = True
            elif t[j] == t[j+k] and flag == True:
                if t[j+k] == 'r':
                    ans += p
                elif t[j+k] == 's':
                    ans += r
                else:
                    ans += s
                flag = False

    print(ans)
main()