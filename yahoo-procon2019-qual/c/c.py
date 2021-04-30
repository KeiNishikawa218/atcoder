
k, a, b = map(int, input().split())

ans = 1
if b - a <= 2:
    print(k + 1)
    exit()
 
times = (k - (a - 1)) // 2
 
if (k - (a - 1)) % 2 == 1:
    print(1 + times * (b - a) + a)
else:
    print(times * (b - a) + a)