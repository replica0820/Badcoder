N = int(input())
A = list(map(int,input().split()))
max_l,max_r = -1,-1
maax = -1 
for l in range(N):
    lmin = A[l]
    cnt = 1
    if maax < A[l]:
            max_l,max_r = l,l
            maax = A[l]
    for r in range(l+1,N):
        lmin = min(lmin,A[r])
        cnt += 1
        if maax < lmin*cnt:
            max_l,max_r = l,r
            maax = lmin*cnt
print(maax)