def Thap(n,a,b,c):
    if n==1:
        print(a+" -> "+c)
        return
    Thap(n-1,a,c,b)
    Thap(1,a,b,c)
    Thap(n-1,b,a,c)

n = int(input())
a,b,c='A','B','C'
Thap(n,a,b,c)
