import sys
import re

# Đọc toàn bộ đầu vào từ sys.stdin
doc = sys.stdin.read()

# Tách văn bản thành các câu, giữ lại dấu câu bằng cách sử dụng nhóm phụ trong biểu thức chính quy.
sentences = re.split('([.?!])', doc)

# Kết hợp lại dấu câu vào câu sau khi tách
sentences = [sentences[i] + sentences[i+1] if i+1 < len(sentences) else sentences[i] for i in range(0, len(sentences), 2)]

# Xử lý mỗi câu một cách riêng biệt.
for sen in sentences:
    if len(sen) == 0: continue  # Bỏ qua các chuỗi rỗng sau khi tách.
    
    # Chuyển đổi tất cả từ trong câu thành chữ thường và chia câu thành các từ.
    sen = sen.lower().split()
    
    # Viết hoa chữ cái đầu tiên của câu.
    sen[0] = sen[0][:1].upper() + sen[0][1:]
    
    # In câu đã chỉnh sửa, nối các từ lại với nhau thành một câu hoàn chỉnh.
    print(' '.join(sen))
