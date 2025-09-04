from collections import defaultdict
N = int(input())
S = defaultdict(int)
A = []
for _ in range(N):
    s,t = input().split()
    A.append((s,t))
    if s != t:
        S[s] += 1
        S[t] += 1
    else:
        S[s]+=1
for x,y in A:
    if S[x] > 1 and S[y] > 1:
        print("No")
        exit()
print("Yes")