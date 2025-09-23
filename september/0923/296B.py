ans = list('abcdefgh')
for i in range(8):
    S = list(input())
    for j in range(8):
        if S[j] == '*':
            print(ans[j],8-i,sep='')
            exit()