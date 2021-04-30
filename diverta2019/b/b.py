r, g, b, n = map(int, input().split())

ans = 0

for i in range(3001):
    for j in range(3001):
        if n - i*r - j*g >= 0 and (n - i*r - j*g) % b == 0 :
            ans += 1

print(ans)