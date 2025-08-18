N = int(input())
a = [(0,0)] * N
for i in range(N):
    q,r = map(int,input().split())
    a[i] = (q,r)
Q = int(input())
for _ in range(Q):
    t,d = map(int,input().split())
    qa,ra = a[t-1]
    yo = (d+qa)%qa
    sa = ra - yo
    print(d + (sa+qa)%qa)