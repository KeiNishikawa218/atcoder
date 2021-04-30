#!/usr/bin/env python3

def main():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]

    ab = sorted(ab, key=lambda x:x[1]) #多次元配列のソートx[]で列を指定

    t = 0

    for i in ab:
        t += i[0]

        if t <= i[1]:
            continue
        else:
            print('No')
            exit()

    print('Yes')
main()