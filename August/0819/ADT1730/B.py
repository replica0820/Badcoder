N = int(input())
H = list(map(int,input().split()))
Takahashi = -1
num = -1
for i in range(N):
    if Takahashi < H[i]:
        num = i+1
        Takahashi = H[i]
print(num)