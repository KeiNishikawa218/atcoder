#!/usr/bin/env python3

def checkStones(p, s):
    if s[p] == '#' and s[p+1] == '#':
        return True
    else:
        return False

def main():
    n, a, b, c, d = map(int, input().split())
    s = list(input())
    s = s + ['#'] + ['#'] + ['#']

    if c < d:
        p2, p1, deepest, shallow = b, a, d, c
    else:
        p2, p1, deepest, shallow = a, b, c, d

    while p2 <= deepest:
        if p2 == deepest: break
        if p1 >= shallow:
            p1 == shallow
            s[p1-1] = '#'
        if s[p2] == '#' and s[p2+1] == '#':
            print('No')
            exit()
        elif s[p2] == '.' and s[p2+1] == '.':
            if p1 == p2+1:
                p2 += 1
            if p1 == p2+2:
                p2 += 0
        elif s[p2] == '.' and s[p2+1] == '#':
            if p2 + 1 == p1:
                if s[p1] == '.': #あり得ない
                    p1 += 1
                elif s[p1+1] == '.':
                    p1 += 2
                elif s[p1] == '#' and s[p1+1] == '#':
                    print('No')
                    exit()
        elif s[p2] == '#' and s[p2+1] == '.':
            if p2 + 2 == p1:
                if s[p1] == '.':
                    p1 += 1
                elif s[p1+1] == '.':
                    p1 += 2
                elif s[p1] == '#' and s[p1+1] == '#':
                    print('No')
                    exit()
            p2 += 1
        if p1 >= shallow:
            p1 == shallow
            s[p1-1] = '#'
        p2 += 1

    while p1 <= shallow:
        if p1 == shallow: break
        if s[p1] == '#' and s[p1+1] == '#':
            print('No')
            exit()
        if s[p1] == '#' and s[p1+1] == '.':
            p1 += 1
        p1 += 1
    print('Yes')
main()