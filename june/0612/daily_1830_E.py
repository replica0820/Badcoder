from collections import defaultdict
N,W = map(int,input().split())
ave = defaultdict(int)
cheese = set()
now = 0
OIC = 0
for i in range(N):
    A,B = map(int,input().split())
    ave[A] += B
    cheese.add(A)
new_c = sorted(cheese,reverse = True)
for j in new_c:
    if now + ave[j] > W:
        OIC += j*(W-now)
        break
    else:
        OIC += j*ave[j]
        now += ave[j]
print(OIC)
