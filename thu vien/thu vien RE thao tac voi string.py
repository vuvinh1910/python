import re
# \d+ la 1 chuoi so vd: 'asd123' thi \d+ la 123
# result = re.findall(r'[a-zA-Z0-9]', s)   cac ky tu tu a-z A-Z va 0-9
# sentences = re.split(r'[.?!]', input_text)  r'[]' la 1 list chua cac ky tu .? ! dung de tach chuoi


# Tìm tất cả các chuỗi con trong chuỗi phù hợp với mẫu và trả về danh sách
result = re.findall(r'\d+', 'abc123def456ghi789')
print(result)  # In ra ['123', '456', '789']

# thay the tat ca cac chuoi con bang ky tu thay the
# re.sub(chuoi_con ,chuoi_thay_the ,chuoi_goc)
result = re.sub(r'\d+', 'X', 'abc123def456')
print(result)  # In ra 'abcXdefX'

result = re.split(r'\d+', 'abc123def456ghi789')
print(result)  # In ra ['abc', 'def', 'ghi', '']

