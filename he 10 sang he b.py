def decimal_to_base(he_10, b):
    digits = "0123456789ABCDEF"
    if he_10 == 0:
        return "0"
    
    result = []
    while he_10 > 0:
        chia_du = he_10 % b
        he_10 = he_10 / b
        he_10 = int(he_10)
        result.append(digits[chia_du])
    
    return ''.join(reversed(result))

# Ví dụ sử dụng
he_10 = 255
b = 8
base_str = decimal_to_base(he_10, b)
print(base_str)  # Output: '377'
