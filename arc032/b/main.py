n, m = map(int, input().split())

#parはparentsの略
# par = [i for i in range(n)]
par = [-1] * n
rank = [-1] * (n)

#木の根を求める
def root(x):
    if par[x] < 0: #親が自分自身
        return x
    else:
        par[x] = root(par[x]) #経路圧縮
        return par[x] 

def same(x, y):
    #イコールならTrueを返す
    return find(x) == find(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    
    # すでに同じ木に属していた場合
    if x == y: return 0

    # 違う木に属していた場合rankを見てくっつける方を決める
    if rank[x] > rank[y]:
        # par[x] += par[y]
        par[y] = x
    elif rank[x] < rank[y]:
        # par[y] += par[x]
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1

for _ in range(m):
    a, b = map(int, input().split())
    unite(a-1, b-1)

res = len(set(par))

for i, x in enumerate(par):
    print(f'{i} {x}')
# print(len(list(set(par[1:])))-1)
print(res-1)