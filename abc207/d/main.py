#!/usr/bin/env python3

def main():
    n = int(input())
    ab = [list(map(int,input().split())) for _ in range(n)]
    cd = [list(map(int,input().split())) for _ in range(n)]

    g1 = [sum([ab[i][0] for i in range(n)])/n, sum([ab[i][1] for i in range(n)])/n]
    g2 = [sum([cd[i][0] for i in range(n)])/n, sum([cd[i][1] for i in range(n)]/n)]

    v1 = [0]*n
    v2 = [0]*n
    
    for i in range(n):
        a, b = ab[i]
        c, d = cd[i]
        v1[i] = (n**2*a**2 - 2*n*a*g1[0] + g1[0]**2) + (n**2*b**2 - 2*n*b*g1[1] + g1[1]**2)
        v2[i] = (n**2*c**2 - 2*n*c*g2[0] + g2[0]**2) + (n**2*d**2 - 2*n*d*g1[1] + g2[1]**2)

    v1.sort()
    v2.sort()
    print(v1)
    print(v2)
    # subAB = [0]*(n-1)
    # a, b = ab[0]

    # for i in range(n-1):
    #     subAB[i] = [ab[i+1][0]-a, ab[i+1][1]-b]

    # subAB.sort()
    # print(subAB)
    # for i in range(n):
    #     c, d = cd[i]
    #     subCD = list(cd[:i] + cd[i+1:])
    #     for j in range(len(subCD)):
    #         subCD[j] = subCD[j][0]-c, subCD[j][1]-d 
    #     subCD.sort()
        
    #     print(subCD)
    #     cnt = 0
    #     for k in range(n-1):
    #         if subAB[k]**2 == list(subCD[k]):
    #             cnt += 1
        
    #     if cnt == n-1:
    #         print('Yes')
    #         exit()

    # print('No')
main()