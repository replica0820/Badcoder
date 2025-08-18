n,m = map(int,input().split())
A = list(map(int,input().split()))
new_A = sorted(A) #10^6回
new_A.append(n+1)
k = max(new_A[0]-1,1)
for i in range(m):
    if new_A[i+1]-new_A[i]-1:
        k = min(new_A[i+1]-new_A[i]-1,k)
count = (new_A[0]-1+k-1)//k
for j in range(m):
    Arange = new_A[j+1]-new_A[j] + k - 2
    mid = Arange//k
    count += mid
    
print(count)
#(A+B-1)//B切り上げ除算
