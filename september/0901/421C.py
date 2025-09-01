N = int(input())
S = list(input())
cnt_A = 0
ansA = 0
ansB = 0
for i in range(2*N):
    if S[i] == 'A':
        cnt_A += 1
        ansA += abs((i+1)-(2*cnt_A))
        ansB += abs((i+1)-(2*cnt_A - 1))
print(min(ansA,ansB))