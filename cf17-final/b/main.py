#!/usr/bin/env python3

def main():

    from collections import Counter
    s = input()
    
    cnt = [0]*3

    for i in s:
        if i == 'a': cnt[0] += 1
        if i == 'b': cnt[1] += 1
        if i == 'c': cnt[2] += 1

    if max(cnt) - min(cnt) <= 1:
        print('YES')
    else:
        print('NO')
main()