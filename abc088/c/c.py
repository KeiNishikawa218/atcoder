arr = [list((map(int,input().split()))) for i in range(3)]

for i in range(min(arr[0])+1):
    a = [0]*3
    a[0] = i    

    b = [j-a[0] for j in arr[0]]

    if arr[1][0] - b[0] == arr[1][1] - b[1] == arr[1][2] - b[2]:
        a[1] = arr[1][0] - b[0]
    else:
        continue

    if arr[2][0] - b[0] == arr[2][1] - b[1] == arr[2][2] - b[2]:
        a[2] = arr[2][0] - b[0]
    else:
        continue

    for k in range(3):
        for l in range(3):
            if a[k] + b[l] == arr[k][l]:
                print('Yes')
                exit()
            else:
                continue
print('No')