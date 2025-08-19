from collections import defaultdict
cnt = defaultdict(int)
person = defaultdict(int)
man = set()
N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    man.add(A[i])
    person[A[i]] = i+1
    cnt[A[i]] += 1
ans = -1
res = -1
for m in man:
    if cnt[m] == 1 and ans < m:
        ans = m
        res = person[m]

print(res)