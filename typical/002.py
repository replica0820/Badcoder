from itertools import product
N = int(input())
if N % 2 == 1:
    exit()
ans = set()
for i in product(['(', ')'],repeat=N):
    cnt = 0
    flag = 1
    for j in range(N):
        if i[j] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            flag = 0
            break
    if flag and cnt == 0:
        print(*i,sep='')