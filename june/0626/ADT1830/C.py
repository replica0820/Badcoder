N = int(input())
A = list(map(int,input().split()))
color = [[] for _ in range(N)]
for i in range(len(A)):
    color[A[i]-1].append(i)
count = 0
for c in color:
    if c[1]-c[0]==2:
        count+=1
print(count)
