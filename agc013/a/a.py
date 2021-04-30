n = int(input())
a = list(map(int, input().split())) 

ans = 0

i = 0
while i < n:
# for i in range(n):
    while i < n-1 and a[i]==a[i+1]:
        i += 1

    #増加
    if i < n-1 and a[i] < a[i+1]:
        while i < n-1 and a[i] <= a[i+1]:
            i += 1
        
    #減少
    elif i < n-1 and a[i] > a[i+1]:
        while i < n-1 and a[i] >= a[i+1]:
            i += 1

    ans += 1
    i += 1

print(ans)