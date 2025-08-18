N = int(input())
A = list(map(int,input().split()))
ans = N
pos = 0
def combi(n):
    return (n+1)*n//2

for i in range(1,N-1):
    if A[i]-A[i-1] != A[i+1]-A[i]:
        ans += combi(i-pos)
        pos = i
ans += combi(N-1-pos)
print(ans)
