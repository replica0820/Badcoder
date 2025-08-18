N = int(input())
A = list(map(int,input().split()))
ans = []
now = 0
for i in range(N):
    sum = 0
    for _ in range(7):
        sum += A[now]
        now += 1
    ans.append(sum)
print(*ans)
    