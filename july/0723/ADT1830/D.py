H,W = map(int,input().split())
sx,sy = -1,-1
ex,ey = -1,-1
now = 1
for i in range(H):
    S = list(input())
    for j in range(W):
        if S[j]=='o' and now:
            sx = i
            sy = j
            now = 0
        if S[j]=='o' and not now:
            ex = i
            ey = j
ans = abs(sx-ex) + abs(sy-ey)
print(ans)
