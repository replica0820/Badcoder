n = int(input())
result = []
for _ in range(n):
    x = list(input())
    result.append(x)
print(result)
for i in range(n):
    for j in range(n):
        if result[i][j] == result[j][i] and result[i][j] == 'D':
            flag = 1
        elif result[i][j] == 'W' and result[j][i] == 'L':
            flag = 1
        elif result[i][j] == 'L' and result[j][i] == 'W':
            flag = 1
        elif i == j:
            flag = 1
        else:
            print("incorrect")
            exit()
print("correct")