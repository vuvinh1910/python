# list.sort(key=None, reverse=False)
# neu xet gia tri key = -1,0,1 thi do uu tien cao nhat sx truoc la -1 roi den 0 roi den 1

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort(key=lambda x: x)  # Sắp xếp tăng dần (mặc định)
print(nums)
# Output: [1, 1, 2, 3, 4, 5, 9]

nums.sort(key=lambda x: -x)  # Sắp xếp giảm dần
print(nums)
# Output: [9, 5, 4, 3, 2, 1, 1]

words = ["apple", "banana", "cherry", "date"]
words.sort(key=lambda x: len(x))  # Sắp xếp theo độ dài chuỗi
print(words)
# Output: ['date', 'apple', 'banana', 'cherry']

words.sort(key=lambda x: x[-1])  # Sắp xếp theo chữ cái cuối cùng
print(words)
# Output: ['banana', 'cherry', 'date', 'apple']


# list.sort(key= lambda x : (first,seconds))  sx theo first truoc sau do sx theo seconds

data = [(1, 2), (1, 3), (2, 2), (2, 1)]
data.sort(key=lambda x: (x[0], -x[1]))    # lambda x : (>2 phan tu so sanh) nen dung dau () de tang hieu suat
print(data)
# Output: [(1, 3), (1, 2), (2, 2), (2, 1)]

nums = [5, 3, 2, 8, 1, 4]
nums.sort(key=lambda x: (x % 2, x))  # so chan truoc, sau do sx tang dan theo x
print(nums)
# Output: [2, 4, 8, 1, 3, 5]

nums = [5, 3, 2, 8, 1, 4]
nums.sort(key=lambda x: (-x if x%2==0 else x))  # so chan giam dan roi so le tang dan
print(nums)
# Output: [2, 4, 8, 1, 3, 5]
