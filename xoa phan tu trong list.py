# remove trong list
so=[1,1,2,3]
so.remove(1) # => 1 2 3

chu["con","con","cu"]
chu.remove("con") # => con cu

list.remove(i) loai 1 phan tu i duoc tim thay dau tien trong ds list

# loai tat ca phan tu target trong ds list
while target in list:
  list.remove(target)

# pop( position ) trong list
lst = ['A', 'B', 'C']
# Xóa phần tử thứ 2 khỏi list
lst.pop(1)
print(lst) # ['A', 'C']

# xoa tat ca phan tu trong list voi clear()
list.clear()

# ham dem so lan phan tu trong list xuat hien
list=[1,1,1,2]
print(list.count(1)) # => 3
