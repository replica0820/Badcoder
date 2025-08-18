N,M = map(int,input().split())
line = [0]*N
all = int(M*(M-1)/2)
for i in range(M):
    A,B = map(int,input().split())
    line_type = (A+B)%M
    line[line_type]+=1
count = 0
for x in line:
    count += int(x*(x-1)/2)
print(all - count)