N,K = map(int,input().split())
A = set(list(map(int,input().split())))
def sqrt_newton(value, sigma):
    
    f = lambda x : x**2 - value
    df = lambda x:2*x

    x0 = 3 # 初期値
    
    while True:
        x = x0 - f(x0) / df(x0)
        if abs(x - x0) < sigma:
            break
        else:
            x0 = x
        
    return x
light = []
marss = []
for i in range(N):
    X,Y = map(int,input().split())
    if (i+1) in A:
        light.append([X,Y])
    else:
        marss.append([X,Y])
max_dis = -1
for m in marss:
    min_m = -1
    for l in light:
        dis = (l[0]-m[0])**2 + (l[1]-m[1])**2
        if min_m == -1:
            min_m = dis
        else:
            min_m = min(min_m,dis)
    max_dis = max(max_dis,min_m)
print(sqrt_newton(max_dis,0.000001))