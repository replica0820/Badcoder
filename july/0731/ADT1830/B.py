N,H,X = map(int,input().split())
P = list(map(int,input().split()))
min_num = 1000
min_index = -1
for i in range(N):
    if H + P[i] >= X:
        if min_num >= P[i]:
            min_num = P[i]
            min_index = i+1
print(min_index)
