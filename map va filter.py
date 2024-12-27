# map(function, (list,string,set,..) )
# function: Hàm cần áp dụng cho (list,string,set,...)
# map se tra ve map object ma khong lam thay doi (list,string,set) da ap dung

a = ['1','2','3']
temp = list(map(int,a))
print(temp) # [1,2,3]


def abs_(n):
  if(n<0):
    n *= -1
  return n

b = [1,2,-3,-4]
b_temp = list(map(abs_,b))
print(b_temp)  # [1,2,3,4]
