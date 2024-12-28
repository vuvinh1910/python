# tach chuoi voi dieu kien de tach bang ham split(ky tu tach chuoi)
# co the thay s tu string thay doi thanh dang danh sach list
s="ha ha ha"
s = s.split(" ") # => ha,ha,ha cai nay chi tach chuoi voi 1 dau cach" "
s= "3    23    32"
s= s.split() # => 3,23,32. cai nay se tach chuoi voi tat ca cac dau cach " "
s="con1cu1bu"
s = s.split("1") # => con,cu,bu

s = input("Nhập chuỗi: ")
s = s.split(" ")  # Tách chuỗi thành danh sách các từ
ds = []
for i in range(len(s)-1, -1, -1):
    ds.append(s[i])
ds = " ".join(ds)  # Nối danh sách ds thành chuỗi, ngăn cách bằng dấu cách
print(ds)

