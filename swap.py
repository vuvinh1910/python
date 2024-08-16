
# luu y quan trong cach nay chi su dung cho bien gia tri so int,float,long
# trong bien
a = 5
b = 10
# Hoán đổi giá trị của a và b
a, b = b, a
print("a =", a)  # Kết quả: a = 10
print("b =", b)  # Kết quả: b = 5

# trong danh sach
lst = [1, 2, 3, 4, 5]
# Hoán đổi phần tử đầu tiên và phần tử cuối cùng
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)  # Kết quả: [5, 2, 3, 4, 1]

