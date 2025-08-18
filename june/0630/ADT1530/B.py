S = list(map(int,input()))
new_S = [0]
new_S.extend(S[:-1])
print(*new_S,sep='')