from functools import cmp_to_key

def custom_sort(x, y):
    if x % 2 == y % 2:  # Nếu cả hai cùng là chẵn hoặc lẻ
        return x - y
    return -1 if x % 2 else 1  # Số lẻ đứng trước số chẵn

nums = [5, 3, 2, 8, 1, 4]
nums.sort(key=cmp_to_key(custom_sort))
print(nums)
# Output: [1, 3, 5, 2, 4, 8]
