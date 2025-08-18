import itertools
N,M = map(int,input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)

def judge(A,B):
    count = 0
    for a,b in zip(A,B):
        if a != b:
            count+=1
    return count

T = list(itertools.permutations(S))
for x in T:
    flag = 1
    for i in range(N-1):
        if judge(x[i],x[i+1]) != 1:
            flag = 0
    if flag:
        print("Yes")
        exit()
print("No")
