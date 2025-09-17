S = list(input())
check = [0] * 26
for s in S:
    check[ord(s)-97] += 1
m = max(check)
for i in range(26):
    if check[i] == m:
        print(chr(i+97))
        exit()