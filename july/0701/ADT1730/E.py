N,M = map(int,input().split())
sum = 0
def bit_count(a):
    return bin(a).count("1")
for i in range(1,N):
    x = i&M
    sum += bit_count(x)
print(sum)