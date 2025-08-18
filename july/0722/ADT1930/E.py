N = int(input())
max_head = 0
high = 0
for _ in range(N):
    A,B = map(int,input().split())
    head = B-A
    max_head = max(head,max_head)
    high += A
print(high + max_head)