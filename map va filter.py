# map(function, (list,string,set,..) )
# function: Hàm cần áp dụng cho (list,string,set,...)
# map se tra ve map object ma khong lam thay doi (list,string,set) da ap dung
def abs_(n):
  if(n<0):
    n *= -1
  return n

def check_abs(n):
  if(n<0):
    return False
  return True

a = ['1','2','3']
temp = list(map(int,a))
print(temp) # [1,2,3]

b = [1,2,-3,-4]
b_temp = list(map(abs_,b))
print(b_temp)  # [1,2,3,4]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Filter
# tuong tu nhu map nhung ham function se tra ve True hoac Flase
# co chuc nang loc ra cac gia tri thoa man trong list,str,set,...
# se tra ve filter obj ma khong lam thay doi danh sach da ap dung

b2_temp = list(filter(check_abs,b))
print(b2_temp)  # [1,2]
