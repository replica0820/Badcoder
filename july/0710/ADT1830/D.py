S = list(input())
cnt = 0
check = [0] * 26
for i in range(26):
    check[ord(S[i]) - 65] = i
now = check[0]
for j in range(26):
    cnt += abs(check[j] - now)
    now = check[j]
print(cnt)