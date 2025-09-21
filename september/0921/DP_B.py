N,K = map(int,input().split())
H = list(map(int,input().split()))
table = [-1] * N
table[0] = 0
for i in range(N-1):
    for n in range(1,K+1):
        if i + n < N:
            if table[i+n] == -1 or table[i] + abs(H[i] - H[i+n]) < table[i+n]:
                table[i+n] = table[i] + abs(H[i] - H[i+n])
print(table[-1])