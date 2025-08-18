n,q = map(int,input().split())
T = list(map(int,input().split()))
tooth = [True] * n
for i in range(q):
    tooth[T[i]-1] = not tooth[T[i]-1]

print(tooth.count(True))