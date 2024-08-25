def ChinhPhuong(a):
    b = int(a**(1/2))
    if b*b == a:
        return True
    else:
        return False
    
def KtraFIBO(t):
    a1 = 5*t*t + 4
    a2 = 5*t*t - 4

    if ChinhPhuong(a1) or ChinhPhuong(a2):
        return True
    else:
        return False

t = int(input())
print(KtraFIBO(t))
