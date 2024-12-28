# [biểu_thức for phần_tử in iterable if điều_kiện]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8]

text = "Hello"
uppercase_letters = [char.upper() for char in text]
print(uppercase_letters)
# Output: ['H', 'E', 'L', 'L', 'O']

test = [1,2,3,4,5,6]
squares = [x**2 for x in test]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
