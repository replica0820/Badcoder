T = list(input())
U = list(input())

lt = len(T)
lu = len(U)
for i in range(lt-lu+1):
    flag = 1
    for j in range(lu):
        if U[j] != T[i+j] and T[i+j] != '?':
            flag = 0
            break
    if flag:
        print("Yes")
        exit()
print("No")