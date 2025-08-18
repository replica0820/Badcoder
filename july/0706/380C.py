N,K = map(int,input().split())
S = list(map(int,input()))
cnt = 0
now = -1
zero = []
one = []
ans = []
for i in range(N):
    if S[i] == 0:
        if now == -1 or now == 1:
            if cnt == K:
                ans.extend(one)
                ans.extend(zero)
            now = 0
        if cnt == K-1:
            zero.append(0)
        else:
            ans.append(0)
    else:
        if now !=1:
            cnt += 1
            now = 1
        if cnt == K:
            one.append(1)
        else:
            ans.append(1)
print(*ans,sep='')