from datetime import datetime

now = datetime.now()

# chuyen datetime sang str
fmd = datetime.strftime(now, "%d/%m/%Y  %H:%M:%S") 
print(fmd)  # 31/12/2024  22:38:21

# chuyen str sang datetime
s = '23/2/2024 1:12:12'
old = datetime.strptime(s, "%d/%m/%Y  %H:%M:%S")
fmd2 = datetime.strftime(old, "%d/%m/%Y  %H:%M:%S") 
print(fmd2)   # 23/02/2024  01:12:12

# co the so sanh datetime bang >,<,==:
print(now>old)  # True

# Tính khoảng cách giữa hai datetime
time_diff = now - old

# In ra kết quả
print("Khoảng cách giữa hai datetime:", time_diff)
print("Số ngày:", time_diff.days)
print("Tổng Số giây:", time_diff.total_seconds())
print("Số giây ko tính ngày chỉ thính theo giờ,phút,giây trong time_diff:", time_diff.seconds)