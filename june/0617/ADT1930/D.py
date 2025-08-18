x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
A = (x2-x1)**2 + (y2-y1)**2
B = (x3-x1)**2 + (y3-y1)**2
C = (x3-x2)**2 + (x3-x2)**2
if A+B == C or A+C == B or B+C == A:
    print("Yes")
else:
    print("No")