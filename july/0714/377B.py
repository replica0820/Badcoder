gridx = [1] * 8
gridy = [1] * 8
for i in range(8):
    S = list(input())
    for j in range(8):
        if S[j] == '#':
            gridx[i] = 0
            gridy[j] = 0
print(sum(gridx) * sum(gridy))