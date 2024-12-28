# tuong tu nhu map, nhung trong python no co ten la dictionary
# gom cac cap key - value

# Tạo dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# dung key truy cap value
print(my_dict["name"])  # Output: Alice

# hoac co the dung ham get de tranh loi neu key khong ton tai
print(my_dict.get("age"))         # Output: 25
# nếu không tìm thấy value tương ứng với key thì sẽ hiển thị giá trị mặc định trong biến thứ 2 của hàm get
print(my_dict.get("job", 90))  # Output: 90

# them cap key-value moi vao tu dien
# cung co the dung de cap nhat gia tri neu da ton tai key
my_dict["job"] = "Engineer"

# xoa 1 cap key-value tron tu dien:
del my_dict["key_name"]

# duyet qua key
for key in my_dict:
    print(key)  # Output: name, age, city

# duyet qua value
for value in my_dict.values():
    print(value)  # Output: Alice, 25, New York

# duyet qua cap key-value
for key, value in my_dict.items():
    print(key, value)
    # Output:
    # name Alice
    # age 25
    # city New York
