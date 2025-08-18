N = int(input())
A = list(map(int,input().split()))
count = 0
ans = []
for i in range(N):
    count = 0
    for j in range(7):
        count += A[i*7 + j]
    ans.append(count)
print(*ans)