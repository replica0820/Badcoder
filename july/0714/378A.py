A = list(map(int,input().split()))
c = [0] * 5
for a in A:
    c[a] += 1
cnt = 0
for x in c:
    if x == 4:
        cnt += 2
    elif x >= 2:
        cnt += 1
print(cnt)