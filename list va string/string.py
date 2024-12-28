# vi tri phan tu trong string
# -1,-2,.. co the dai dien cho vi tri cuoi cua string
s = "12345"
s[0]=1
s[-1]=5
s[-2]=4

# do dai chuoi
s="concubu"
len(s)

# lưu ý là các chuỗi trong Python là bất biến (immutable), 
# có nghĩa là chúng không thể thay đổi sau khi được tạo
# muon thay doi thi lam nhu sau: s = s.lower() , neu chi ghi s.lower() thi s khong thay doi

# chuyen chuoi thanh in hoa
s=s.upper()
# chuyen chuoi thanh in thuong
s=s.lower()
# kiem tra chuoi chua toan ky tu chu hay khong
ktra = s.isalpha() # true hoac false
# kiem tra chuoi chua toan so hay khong
ktra = s.isnumeric() # true hoac false

