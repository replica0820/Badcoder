N = int(input())
a = [[1]]
print(1)
for i in range(1,N):
    tmp = [1]
    if i > 1:
        for j in range(1,i):
            tmp.append(a[i-1][j-1]+a[i-1][j])
    tmp.append(1)
    a.append(tmp)
    print(*tmp)
