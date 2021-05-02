s = input()

length = len(s)

ans = (length - 1) * 2

for i in range(1, length-1):
    if s[i] == 'U':
        ans += (length-1-i) + i*2
    else:
        ans += (length-1-i)*2 + i

print(ans)