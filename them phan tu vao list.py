# append() thêm một phần tử vào cuối danh sách
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)  # Kết quả: ['apple', 'banana', 'cherry']
# append() cung co the them ds vao cuoi ds, nhung ds duoc them se chuyen thanh 1 phan tu
# vd "1","2" thanh "1 2"

# extend() thêm ds chon vao cuoi ds muc tieu
fruits = ['apple', 'banana']
more_fruits = ['cherry', 'date']
fruits.extend(more_fruits)
print(fruits)  # Kết quả: ['apple', 'banana', 'cherry', 'date']

# insert() chèn một phần tử vào một vị trí cụ thể trong danh sách
# list.insert(vitri, phantu)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'blueberry')
print(fruits)  # Kết quả: ['apple', 'blueberry', 'banana', 'cherry']

# dung +=
fruits = ['apple', 'banana']
more_fruits = ['cherry', 'date']
fruits += more_fruits
print(fruits)  # Kết quả: ['apple', 'banana', 'cherry', 'date']


