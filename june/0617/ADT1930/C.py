N = int(input())
sum = 0
name = []
for _ in range(N):
    S,C = input().split()
    name.append(S)
    sum += int(C)
rate = sum%N
sorted_name = sorted(name)
print(sorted_name[rate])