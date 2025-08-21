H,W = map(int,input().split())
table = []
for _ in range(H):
    A = list(map(int,input().split()))
    table.append(A)
for i1 in range(H):
    for i2 in range(i1,H):
        for j1 in range(W):
            for j2 in range(j1,W):
                if table[i1][j2] + table[i2][j1] < table[i1][j1] + table[i2][j2]:
                    print("No")
                    exit()
print("Yes")