h = int(input())

n = 1
ans = 1

while h > 1:
    n *= 2 
    ans += n
    h = h//2

print(ans) 