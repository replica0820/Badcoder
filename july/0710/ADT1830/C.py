N = int(input())
A = list(map(int,input().split()))
count = set()
for a in A:
    count.add(a)
print(len(count))