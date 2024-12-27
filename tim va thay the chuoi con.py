s1 = input()
s2 = input()
while(s2 in s1):
    s1 = s1.replace(s2,'')
print(s1)
