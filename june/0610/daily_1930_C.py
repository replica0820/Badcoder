M = int(input())
a = []
n = M
j = 0
count = 0
while n!=0:
    x = n%3
    for _ in range(x):
        a.append(j)
        count+=1
    n = n //3
    j+=1

print(count)
print(*a)

#方針：3進数にして小さいほうから答える。