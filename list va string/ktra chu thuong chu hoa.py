# Bạn có thể kiểm tra một ký tự là in thường hay in hoa bằng hàm isupper() và islower()
def show(s):
    lw,up=0,0
    for i in s:
        if i.islower():
            lw+=1
        elif i.isupper():
            up+=1
    print("Given string:",s)
    print("Number of uppercase letters:",up)
    print("Number of lowercase letters:",lw)


s = str(input())
show(s)
