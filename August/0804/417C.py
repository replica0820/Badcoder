from collections import defaultdict
from itertools import combinations
N = int(input())
A = list(map(int,input().split()))
B = defaultdict(int)
C = defaultdict(int)
BS = set()
CS = set()
for i in range(N):
    X = A[i] + (i+1)
    Y = (i+1) - A[i]
    B[X] += 1
    BS.add(X)
    C[Y] += 1
    CS.add(Y)
cnt = 0
for b in BS:
    if b in CS:
        cnt += (B[b]*C[b])
print(cnt)