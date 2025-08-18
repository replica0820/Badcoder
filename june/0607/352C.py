n = int(input())
max_head = 0
height = 0
for i in range(n):
    A,B = map(int,input().split())
    head = B - A
    max_head = max(max_head,head)
    height += A
height += max_head
print(height)