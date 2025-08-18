n,k,x = map(int,input().split())
A = list(map(int,input().split()))

A.insert(k,x)
print(*A)