n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i:] == t[:n-i]:
        print(n-i)
        eixt()

print(n*2)