N = int(input())
A = list(map(int,input().split()))
print(0)
ans = [0] * (N+1)
for i in range(N):
    mom = A[i]//2
    gen = i+1
    ans[gen] = ans[mom] + 1
    print(ans[gen])
    print(ans[gen])