n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i:] == t[:n-i]:
        print(2*n-(n-i))
        exit()

print(n*2)