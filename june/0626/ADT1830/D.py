N,K = map(int,input().split())
A = list(map(int,input().split()))
limit = 10**K
monitor = 1
for a in A:
    monitor *= a
    if monitor >= limit:
        monitor = 1
print(monitor)