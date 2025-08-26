H,W = map(int,input().split())
for _ in range(H):
    S = list(input())
    ans = S[:]
    for i in range(W):
        if ans[i] == 'T' and ans[i+1] == 'T':
            ans[i] = 'P'
            ans[i+1] = 'C'
    print(*ans,sep='')