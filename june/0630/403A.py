N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(0,N,2):
    cnt += A[i]
print(cnt)