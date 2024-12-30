m = 10**9+7

def pow(a,b,m):
    if(b==0): return 1
    if(b==1): return a
    temp = pow(a,b//2,m)
    if(b%2==1):
        return (temp%m * temp%m * a) % m
    else:
        return temp%m * temp%m