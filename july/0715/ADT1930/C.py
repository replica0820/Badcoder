N = int(input())
X = sorted(list(map(int,input().split())))
s = 0
for x in X[N:4*N]:
    s += x
print(s/(3*N))
