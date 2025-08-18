import heapq
from collections import defaultdict
maax = []
miin = []
Q = int(input())
a = defaultdict(int)
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x = query[1]
        a[x] += 1
        heapq.heappush(maax,-x)
        heapq.heappush(miin,x)
    elif query[0] == 2:
        x = query[1]
        c = query[2]
        for _ in range(min(c,a[x])):
            a[x] = max(0,a[x]-c)
    else:
        while a[-maax[0]] == 0:
            heapq.heappop(maax)
        while a[miin[0]] == 0:
            heapq.heappop(miin)
        print(-maax[0]-miin[0])