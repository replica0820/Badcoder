S = list(input())
check = [0] * 26
for i in S:
    check[ord(i)-97] += 1
for j in range(len(check)):
    if check[j] == 1:
        print(chr(j+97))
        exit()
print(-1)