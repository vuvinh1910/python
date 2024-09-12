round(number, ndigits)
#Trong đó number là số cần làm tròn, ndigits là số chữ số sau dấu phẩy cần làm tròn

vd:
n = int(input())
count = 0
for i in range(1,n+1):
    count += i/(i+1)
print(round(count,2))


tong = 3.144444444
print(f"{tong:.6f}")
# in ra 6 số sau dấu phẩy ko làm tròn
