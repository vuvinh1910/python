my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
my_list = list(set(my_list)) # đưa về set loại trùng lặp rồi chuyển về list
print(my_list)  # Output: [1, 2, 3, 4, 5]
