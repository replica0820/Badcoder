n = int(input())
A = list(map(int,input().split()))
ans = []
mid = [-1] * n

for i in range(n):
    if A[i] == -1:
        j = i
    else:
        mid[A[i]-1] = i
while j >= 0:
    ans.append(j+1)
    j = mid[j]
print(*ans)