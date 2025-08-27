from itertools import combinations
H,W = map(int,input().split())
cH = [i for i in range(H)]
cW = [i for i in range(W)]
mapA = []
for _ in range(H):
    A = list(map(int,input().split()))
    mapA.append(A)
H2,W2 = map(int,input().split())
if H < H2 or W < W2:
    print("No")
    exit()
mapB = []
for _ in range(H2):
    B = list(map(int,input().split()))
    mapB.append(B)

for i in combinations(cH,H2):
    for j in combinations(cW,W2):
        flag = 1
        for x in range(H2):
            for y in range(W2):
                if mapA[i[x]][j[y]] != mapB[x][y]:
                    flag = 0
        if flag:
            print("Yes")
            exit()
print("No")