N = int(input())
H = list(map(int,input().split()))
table = [-1] * N
table[0] = 0
next = [1,2]
for i in range(N-1):
    for n in next:
        if i + n < N:
            if table[i+n] == -1 or table[i] + abs(H[i] - H[i+n]) < table[i+n]:
                table[i+n] = table[i] + abs(H[i] - H[i+n])
print(table[-1])