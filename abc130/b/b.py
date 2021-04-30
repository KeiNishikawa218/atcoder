n, x = map(int, input().split())
ll = list(map(int, input().split())) 

ans = 1
d_p = 0
d_c = 0

for i in range(n):
    d_c = d_p + ll[i]
    if d_c <= x:
        ans += 1

    d_p = d_c

print(ans) 