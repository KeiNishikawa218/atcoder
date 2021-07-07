#!/usr/bin/env python3

def main():
    s = input()
    t = input()

    ans = 0

    for i in range(len(s) - len(t) + 1):
        res = 0

        for j in range(len(t)):
            if s[i+j] == t[j]:
                res += 1

        ans = max(ans, res)

    print(len(t) - ans)
main()