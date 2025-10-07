N = int(input())
res = []
for _ in range(N):
    A = list(input())
    res.append(A)

for i in range(N):
    for j in range(i+1,N):
        if not ((res[i][j] == 'W' and res[j][i] == 'L') or (res[i][j] == 'L' and res[j][i] == 'W') or (res[i][j] == 'D' and res[j][i] == 'D')):
            print("incorrect")
            exit()
print("correct")