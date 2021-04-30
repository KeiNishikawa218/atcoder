n, x = map(int, input().split())
ll = list(map(int, input().split())) 

d = 0

for i in ll:
    d += d + i

print(d)