N,Q = map(int,input().split())
X = list(map(int,input().split()))
box = [0] * N
ans = []
for i in range(Q):
    if X[i] >= 1:
        box[X[i]-1] += 1
        ans.append(X[i])
    else:
        min_box = 1
        min_count = box[0]
        for j in range(1,N):
            if min_count > box[j]:
                min_box = j+1
                min_count = box[j]
        box[min_box-1] += 1
        ans.append(min_box)

print(*ans)
    