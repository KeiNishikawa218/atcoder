#!/usr/bin/env python3

def main():
    n, a, b, c, d = map(int, input().split())
    s = list(input().split())) 
    s = s + ['#'] + ['#']

    print(s)
    if c < d:
        last, secondFromLast, deepest = b, a, d
    else:
        last, secondFromLast, deepest = a, b, c

    for i in range(min(deepest, n-2)):
        if s[last] == '#' and s[last+1] == '#':
            print('No')

main()