n, k = map(int,input().split())
S = h=list(input().split())
count = 0
for i in range(0,n-k):
  a = i
  b = i + k - 1
  if a < b:
    if S[a] == S[b] or S[a] == '?' or S[b] =='?':
      a += 1
      b -= 1
    else:
      break
    if a == b or a == b + 1:
      count +=1
print(count)