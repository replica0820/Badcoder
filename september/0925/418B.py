S = list(input())
N = len(S)
ans = 0
for i in range(N):
    for j in range(i,N):
        leng = j - i + 1
        check = S[i:j+1]
        cnt = check.count('t')
        if leng >= 3:
            o = (cnt-2)/(leng-2)
            ans = max(ans,o)
print(ans)