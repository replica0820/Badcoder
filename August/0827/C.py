N = int(input())
check = []
for _ in range(N):
    S = list(input())
    check.append(S)

for i in range(N):
    for j in range(N):
        if i != j:
            test = check[i] + check[j]
            if test == test[::-1]:
                print("Yes")
                exit()
print("No")