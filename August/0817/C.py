R = []
C = []
N = int(input())
for _ in range(N):
    r,c = map(int,input().split())
    R.append(r)
    C.append(c)
R.sort()
C.sort()

tr = (R[-1]+R[0])//2
tc = (C[-1]+C[0])//2

ans = 0
for i in range(N):
    ans = max(ans,abs(tr-R[i]))
    ans = max(ans,abs(tc-C[i]))
print(ans)