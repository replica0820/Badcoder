N = int(input())
q = [0] * N
p = list(map(int,input().split()))
for i in range(N):
    q[p[i]-1] = i+1
print(*q)