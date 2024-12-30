import re
s=''

# doc luong van ban
while(True):
    try:
        s += input()
    except Exception:
        break



s = s.strip()
lst = re.split(r'[.?!]',s)
for i in lst:
    i = re.sub(r'\s+',' ',s)
    i = i.capitalize()
    print(i)
