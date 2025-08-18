N,L,R = map(int,input().split())
S = list(input())
for i in range(L-1,R):
    if S[i] == 'x':
        print("No")
        exit()
print("Yes")