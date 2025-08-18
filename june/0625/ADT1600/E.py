N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())),reverse=True)
ans = -1
i,j = 0,0
while 1:
    if i ==N:
        break
    elif j == N-1:
        ans = A[-1]
        break
    if A[i] > B[j]:
        if ans != -1:
            print(-1)
            exit()
        else:
            ans = A[i]
            j-=1
    i+=1
    j+=1
print(ans)

