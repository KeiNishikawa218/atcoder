n = int(input())
a = [int(input()) for i in range(n)]

a.sort()
ans = 0

ptr = 0
while ptr < n:
    cc = a[ptr]
    f = 0

    while ptr < n and a[ptr]==cc:
        f += 1
        ptr += 1

    ans += f%2

print(ans)