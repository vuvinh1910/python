# 1. Tìm min và max trong một danh sách:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Min:", min(numbers))  # Kết quả: Min: 1
print("Max:", max(numbers))  # Kết quả: Max: 9
# 2. Sử dụng min và max với nhiều đối số:
a = 10
b = 20
c = 5
print("Min:", min(a, b, c))  # Kết quả: Min: 5
print("Max:", max(a, b, c))  # Kết quả: Max: 20
# 3. Tìm min và max trong một chuỗi:
s = "hello"
print("Min:", min(s))  # Kết quả: Min: 'e'
print("Max:", max(s))  # Kết quả: Max: 'o'

# Bạn cũng có thể sử dụng từ khóa key để chỉ định một hàm làm tiêu chí so sánh. Ví dụ, để tìm chuỗi dài nhất trong một danh sách các chuỗi:
words = ["apple", "banana", "cherry"]
longest_word = max(words, key=len)
print("Longest word:", longest_word)  # Kết quả: Longest word: banana
