#!/usr/bin/env python3

def main():
    n = int(input())
    st = [list(input().split()) for _ in range(n)]

    st = [[i[0], int(i[1])] for i in st]
    st = sorted(st, key=lambda x:x[1]) #多次元配列のソートx[]で列を指定

    print(st[-2][0])

main()