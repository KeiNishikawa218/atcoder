#!/usr/bin/env python3

def main():
    from collections import Counter

    s = input()

    if len(s) == 1 or len(s) == 2:
        if int(s)%8 == 0 or int(s[::-1])%8 == 0:
            print('Yes')
        else:
            print('No')
        exit()

    s2 = Counter(s)

    for n in range(112, 1000, 8):
        if not Counter(str(n)) - s2:
            print('Yes')
            exit()
    
    print('No')
main()