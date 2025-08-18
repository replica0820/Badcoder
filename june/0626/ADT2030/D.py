S = list(input())
T = list(input())
N = len(S)
flag = 0
i=0
while i < N:
    if S[i] != T[i]:
        if S[i] != T[i+1] or S[i+1]!=T[i] or flag:
            print("No")
            exit()
        i+=1
    i+=1
print("Yes")