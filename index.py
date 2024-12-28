# Áp dụng cho: Dùng được cho cả chuỗi (str) và danh sách (list)
s = "hello world"
position = s.index("world")  # Trả về 6
position = s.index("Python") # Gây ra lỗi ValueError vì ko tồn tại.
