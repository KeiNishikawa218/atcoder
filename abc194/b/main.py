#!/usr/bin/env python3

def main():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]

    a = [ab[i][0] for i in range(n)]
    b = [ab[i][1] for i in range(n)]

    #A, Bの最小値
    minA, minB = min(a), min(b)

    #同一人物か判定
    workerA = a.index(min(a))
    workerB = b.index(min(b))

    if workerA != workerB:  #別人
        print(max(min(a), min(b)))
    else:                   #同一人物          
        secondMinA = sorted(a)[1]
        secondMinB = sorted(b)[1]

        if minA + minB <= max(a[workerA], secondMinB): #同一人物に任せた方が速い
            print(minA + minB)
        elif minA + minB <= max(secondMinA, b[workerB]): #同一人物に任せた方が速い
            print(minA + minB)
        else: #同一人物に任せた方が遅い
            print(min(max(a[workerA], secondMinB), max(secondMinA, b[workerB])))

main()