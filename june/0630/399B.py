N = int(input())
P = list(map(int,input().split()))
new_P = sorted(P,reverse=True)
for i in range(N):
    print(new_P.index(P[i])+1)