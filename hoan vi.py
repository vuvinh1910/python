from itertools import permutations

# Nhập chuỗi từ người dùng
s = input().strip()

# Tạo tất cả các hoán vị
perm_list = permutations(s)

# In từng hoán vị
for perm in perm_list:
    print(''.join(perm))
