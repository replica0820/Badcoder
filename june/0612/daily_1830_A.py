A,B,C,D,E,F,X = map(int,input().split())
T_time = X%(A+C)
A_time = X%(D+F)
T_count = X//(A+C)
A_count = X//(D+F)
T_dis = (A*T_count+min(T_time,A))*B
A_dis = (D*A_count+ min(A_time,D))*E
if T_dis>A_dis:
    print("Takahashi")
elif T_dis == A_dis:
    print("Draw")
else:
    print("Aoki")