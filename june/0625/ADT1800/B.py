S = list(input())
n = len(S)
if S[0] == '<' and S[-1] == '>':
    for i in range(1,n-1):
        if S[i] != '=':
            print("No")
            exit()
    print("Yes")
    exit()
print("No")
