N = int(input())
P = list(map(int,input().split()))
P.append(-1)

count = 0
ans = []
for i in range(0,N):
    if P[i] < P[i+1]:
        count += 1
    elif count > 0:
        ans.append(count)
        count = 0
s,t = 0,0
for i in ans:
    s += t * i
    t = i
print(s)