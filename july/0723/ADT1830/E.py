N,K = map(int,input().split())
f = [1]*K
a = K
f.append(a)
cnt = 0
m = 10**9
for i in range(K,N):
    a-=f[cnt]
    cnt+=1
    a+=f[-1]
    a%=m
    f.append(a)
print(f[N])