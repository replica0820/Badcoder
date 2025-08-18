def nbtn(num, lets, x):
    l = 0
    r = num
    while l < r:
        m = (l + r) // 2
        if lets[m] < x:
            l = m + 1
        else:
            r = m
    return l

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

sumA = [0] * N
sumA[0] = A[0]
for j in range(1, N):
    sumA[j] = sumA[j-1] + A[j]

for _ in range(Q):
    B = int(input())
    if B > A[-1]:
        print(-1)
        continue
    cnt = nbtn(N, A, B)
    x = 1
    if cnt > 0:
        x += sumA[cnt-1]
    x += (N - cnt) * (B - 1)
    print(x)
