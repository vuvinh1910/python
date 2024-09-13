from itertools import permutations

# Nhập chuỗi từ người dùng
s = input().strip()

# Tạo tất cả các hoán vị
perm_list = permutations(s)

# In từng hoán vị
for perm in perm_list:
    print(''.join(perm)) # perm la mot set trong perm_list

# Kiểm tra và in hoán vị thứ 3 nếu có
if len(perm_list) >= 3:
    third_permutation = ''.join(perm_list[2])
    print(third_permutation)
else:
    print("Không đủ hoán vị")
