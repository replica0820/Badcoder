N = int(input())
A = sorted(set(map(int,input().split())))
print(len(A))
print(*A,sep=' ')