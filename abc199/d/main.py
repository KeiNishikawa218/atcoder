#!/usr/bin/env python3
class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正==子: 根の頂点番号 / 負==根: 連結頂点数

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.size(x) < self.size(y):
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parent[x]

    def is_root(self, x):
        return self.parent[x] < 0

def main():
    n, m = map(int, input().split())
    count = 0
    pair_list = []
    uf = UnionFind(n)
    for i in range(m):
        array = list(map(int,input().split()))
        array[0] -=1 ; array[1] -= 1
        pair_list.append(array)
        print(uf.unite(n-1,m-1))


main()