decimal_number = 10
binary_str = bin(decimal_number)[2:]  # Loại bỏ '0b'
print(binary_str)  # Output: '1010'

decimal_number = 255
hex_str = hex(decimal_number)[2:].upper()  # Loại bỏ '0x' và chuyển thành chữ hoa
print(hex_str)  # Output: 'FF'
