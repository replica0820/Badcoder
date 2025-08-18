N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
ans = min(abs(A[-1] - B[-1]),abs(A[0]-B[0]))
i,j = 0,0
while 1:
    if i >= N-1 and j >= M-1:
        break
    elif i >= N -1:
        j+=1
    elif j >= M-1:
        i +=1
    elif A[i] > B[j]:
        j+=1
    else:
        i += 1
    ans = min(ans,abs(A[i]-B[j]))
print(ans)