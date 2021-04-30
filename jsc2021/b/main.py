#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 

    #2つのリストから共通しない要素を抽出
    l1_l2_sym_diff = list(set(a) ^ set(b))

    ans = list(sorted(l1_l2_sym_diff))
    print(*ans)
main()