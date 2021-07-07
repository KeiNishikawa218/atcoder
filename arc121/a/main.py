#!/usr/bin/env python3

def main():
    n = int(input())
    xy = [list(map(int,input().split())) + [i] for i in range(n)]

    # n = 5
    # xy = [[0,0], [6,0], [0,0], [0,0], [0,0]]
    # xy = [[0,2], [1,1], [2,0]]
    Dx = sorted(xy, key=lambda x:x[0]) #多次元配列のソートx[]で列を指定
    Dy = sorted(xy, key=lambda x:x[1]) #多次元配列のソートx[]で列を指定

    Dx = Dx[0:2] + Dx[-2:]
    Dy = Dy[0:2] + Dy[-2:]
    # ll = [abs(Dx[-1][0]-Dx[0][0]), abs(Dy[-1][1]-Dy[0][1]), abs(Dx[-2][0]-Dx[0][0]), abs(Dx[-1][0]-Dx[1][0]), abs(Dy[-2][1]-Dy[0][1]), abs(Dy[-1][1]-Dy[1][1])]

    def get_unique_list(seq):
        seen = []
        return [x for x in seq if x not in seen and not seen.append(x)]

    DD = get_unique_list(Dx+Dy)

    res = []

    for i in range(len(DD)-1):
        for j in range(i+1, len(DD)):
            # print(f'{abs(DD[i][0]-DD[j][0])} {abs(DD[i][1]-DD[j][1])}')
            res.append(max(abs(DD[i][0]-DD[j][0]), abs(DD[i][1]-DD[j][1])))

    res.sort(reverse=True)
    print(res[1])
    # print(sorted(ll)[-2])

main()