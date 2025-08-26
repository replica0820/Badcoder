N = int(input())
result = []
for _ in range(N):
    A = list(input())
    result.append(A)
for i in range(N):
    for j in range(i+1,N):
        if (result[i][j] == 'W' and result[j][i] != 'L') or (result[i][j] == 'L' and result[j][i] != 'W') or (result[i][j] == 'D' and result[j][i] != 'D'):
            print("incorrect")
            exit()
print("correct")
    