#!/usr/bin/env python3

def main():
    S = input()

    ans = [0]*6

    for s in S:
        if s == 'A':
            ans[0] += 1
        elif s == 'B':
            ans [1] += 1
        elif s == 'C':
            ans [2] += 1
        elif s == 'D':
            ans [3] += 1
        elif s == 'E':
            ans [4] += 1
        elif s == 'F':
            ans [5] += 1

    print(*ans)


main()