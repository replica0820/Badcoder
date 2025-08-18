N = int(input())
now,cnt = map(int,input().split())
for _ in range(1,N):
    T,V = map(int,input().split())
    cnt = max((cnt-(T-now)),0)
    cnt += V
    now = T
print(cnt)
    
    