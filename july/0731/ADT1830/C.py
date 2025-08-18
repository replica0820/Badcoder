N,M = map(int,input().split())
more_strong = [0] * N
for _ in range(M):
    A,B = map(int,input().split())
    more_strong[B-1] = 1
x = more_strong.count(0)
if x != 1:
    print(-1)
else:
    print(more_strong.index(0)+1)