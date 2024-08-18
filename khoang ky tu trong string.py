# in ra khoang trong chuoi print(s[value_a : value_b]) khong bao gom value_b (value_a den value_b-1)
x="Python"
print(x[1:3]) # => py
print(x[2:]) # in ra tu vi tri 2 den het xau

# lap lai chuoi
x="CodeLearn"
print(x*2) # => CodeLearnCodeLearn

# cach dung s[start,end]
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
