s = "hello hello hello"

# Tìm kiếm "hello" bắt đầu từ vị trí 5
print(s.find("hello", 5))  # Kết quả: 6 (bắt đầu từ vị trí 6)

# Tìm kiếm "hello" trong khoảng từ vị trí 7 đến 15
print(s.find("hello", 7, 15))  # Kết quả: -1 (vì không có "hello" trong đoạn này)
