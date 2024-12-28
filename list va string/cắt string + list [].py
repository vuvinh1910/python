# in ra khoang trong chuoi print(s[start : end]) khong bao gom end (start den end-1)
x="Python"
print(x[1:3]) # => py
print(x[2:]) # in ra tu vi tri 2 den het xau

lst = [1,2,3,4,5]
print(lst[-2:])  # 4,5

# lap lai chuoi
x="CodeLearn"
print(x*2) # => CodeLearnCodeLearn

# cach dung s[start,end,step_defalut=1]
s = str(input())
def format(s):
    if len(s) < 3:
        print(s)
    elif s[-3:] != "ing": # 3 ky tu cuoi cung trong chuoi string
        new_s= s[0:] + "ing"
        print(new_s)
    else:
        new_s= s[0:] + "ly"
        print(new_s)
format(s)
