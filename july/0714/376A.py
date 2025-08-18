N,C = map(int,input().split())
T = list(map(int,input().split()))
now = T[0]
cnt = 1
for i in range(1,N):
    if T[i] > now + C:
        print(T[i],now)
        cnt += 1
        now = T[i]
print(cnt)