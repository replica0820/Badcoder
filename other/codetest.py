n,s = map(int,input().split())
A = list(map(int,input().split()))

for i in range(1,n):
  if A[i] - A[i-1] >= s + 0.5:
    print("No")
    exit()
    
print("Yes")