#!/usr/bin/env python3

def main():
    s = input()

    ans = 10*5

    for c in set(s):
        t = s
        cnt = 0
        while len(set(t)) != 1:
            u = ''
            for i in range(len(t) - 1):
                if t[i] == c or t[i+1] == c:
                    u += c
                else:
                    u += t[i]

            t = u
            cnt += 1
            # print(s)
            # print(cnt)
        ans = min(ans, cnt)
    print(ans)
main()