N,M = map(int,input().split())
A = list(map(int,input().split()))
check = set()
cnt = 0
for i in range(N):
    if A[i] not in check:
        cnt += 1
        check.add(A[i])
    if cnt == M:
        print(N - i)
        exit()
print(0)