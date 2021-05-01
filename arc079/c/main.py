#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]

    list1 = []
    list2 = []

    for i in range(m):
        if ab[i][0] == 1:
            list1.append(ab[i][1])
        if ab[i][1] == n:
            list2.append(ab[i][0])

    lists_and = set(list1) & set(list2)

    if len(lists_and) > 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
main()