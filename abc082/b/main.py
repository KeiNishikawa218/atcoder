#!/usr/bin/env python3

def main():
    s = sorted(input())
    t = sorted(input(), reverse = True)

    s = ''.join(s)
    t = ''.join(t)

    if s < t:
        print('Yes')
    else:
        print('No')
main()