A,B,C = map(int,input().split())
if A==B==C or A+B == C or A == B+C or B == A+C:
    print("Yes")
else:
    print("No")