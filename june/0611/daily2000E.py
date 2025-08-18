n,m = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
if s <= m:
    print("infinite")
    exit()
left = 0
right = 10**9
while abs(left-right)>1:
  mid = (left+right)//2
  sum = 0
  for j in range(n):
    sum +=  min(A[j],mid)
  if sum <= m:
    left = mid
  else:
    right = mid
print(left)