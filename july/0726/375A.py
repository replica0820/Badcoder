N = int(input())
S = input()
cnt = 0
for i in range(1,N-1):
    if S[i-1] == '#' and S[i] == '.' and S[i+1] == '#':
        cnt += 1
print(cnt)
