N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
a = N - M + 1
for i in range(a):
    for j in range(a):
        ok = 1
        for x in range(M):
            for y in range(M):
                if S[i+x][j+y] != T[x][y]:
                    ok = 0
        if ok:
            print(i+1,j+1)
