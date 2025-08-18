def trial_odd_sqrt(n: int):
    assert n > 1
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= n**0.5:
        if n%i == 0:
            return False
        i+=2
    return True

n = input()
a = list((map(int,n)))
n = int(n)
if n == 1:
    print("Not Prime")
elif trial_odd_sqrt(n) or (a[-1] != 5 and a[-1]%2 != 0 and sum(a)%3 != 0):
    print("Prime")
else:
    print("Not Prime")