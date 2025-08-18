N,D = map(int,input().split())
NG = [1] * D
mcount = 0
count = 0
for _ in range(N):
    S = list(input())
    for i in range(D):
        if S[i] == 'x':
            NG[i] = 0
for j in range(D):
    if NG[j] == 1:
        count += 1
        mcount = max(mcount,count)
    else:
        count = 0
    mcount = max(mcount,count)
print(mcount)