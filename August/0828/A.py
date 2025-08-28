N = int(input())
S = list(input())
T = list(input())
for i in range(N):
    if not(S[i] == '1' and T[i] == 'l' or S[i] == 'l' and T[i] == '1' or S[i] == 'o' and T[i] == '0' or S[i] == '0' and T[i] == 'o' or S[i] == T[i]):
        print("No")
        exit()
print("Yes")