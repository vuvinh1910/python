import itertools

s=[9,3,4]
s.sort()
per = itertools.permutations(s)   # trả về danh sách chứa các dãy hoán vị
for i in per:
    print(' '.join([str(x) for x in i]))

for i in per:
    print(' '.join(map(str,i)))