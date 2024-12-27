import math
# round(number, ndigits)
#Trong đó number là số cần làm tròn, ndigits là số chữ số sau dấu phẩy cần làm tròn
# vd:
n = 12.88888
print(int(round(n,0))) # ket qua = 13
print(round(n,3)) # ket qua = 12.889

# lam tron bang f-print
tong = 3.17777777
print(f"{tong:.6f}")  # in ra 6 số sau dấu phẩy co làm tròn

# lam tron len den phan nguyen
print(math.ceil(tong)) # ket qua = 4

# lam tron xuong den phan nguyen
print(math.floor(n)) # ket qua = 12
