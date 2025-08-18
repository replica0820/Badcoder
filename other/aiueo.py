n = int(input())
x = [] * n
result = []
cost = -1
for i in range(n):
    a = list(map(int,input().split()))
    a.append(i+1)
    x.append(a)
ans = sorted(x,reverse=True)

for j in range(n):
    if j == 0:
        result.append(ans[j][2])
        cost = ans[j][1]
    else:
        if cost > ans[j][1]:
            result.append(ans[j][2])
            cost = ans[j][1]
print(len(result))
aa = sorted(result)
print(*aa)