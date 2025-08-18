N,M = map(int,input().split())
A = list(map(int,input().split()))
ans = []
for i in range(1,N+1):
    flag = 1
    for a in A:
        if i == a:
            flag = 0
            break
    if flag:
        ans.append(i)
print(len(ans))
print(*ans)