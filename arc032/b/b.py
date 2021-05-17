n, m = map(int, input().split())

par = [i for i in range(n+1)]

#木の根を求める
def root(x):
    if par[x] == x:
        return x
    else:
        return par[x] = root(par[x])

def same(x, y):
    if root(x) == root(y):
        return 0
    else:
        return 1

def unite(x, y):
    x = root(x)
    y = root(y)
    
    if x == y: return

    par[x] = y

for _ in range(m):
    a, b = map(int, input().split())
    unite(a, b)

print(par)