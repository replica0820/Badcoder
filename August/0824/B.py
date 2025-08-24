N,M = map(int,input().split())
S = []
pnt = [0]*N
for _ in range(N):
    s = list(map(int,input()))
    S.append(s)
for i in range(M):
    one_cnt = 0
    one_per = []
    zero_cnt = 0
    zero_per = []
    for j in range(N):
        if S[j][i]:
            one_cnt += 1
            one_per.append(j)
        else:
            zero_cnt += 1
            zero_per.append(j)
    if one_cnt > zero_cnt:
        for z in zero_per:
            pnt[z] += 1
    else:
        for o in one_per:
            pnt[o] += 1
line = max(pnt)
for y in range(N):
    if pnt[y] == line:
        print(y+1,end=' ')
