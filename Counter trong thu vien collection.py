import collections
a = [1,1,2,2,2,3,3,3]
cnt = collections.Counter(a)
co the unpack cnt sang dict hoac list hoac set
print(cnt.keys(),cnt.values(),cnt.items())

s = 'con cac'
print(collections.Counter(s))
# Counter({'c': 3, 'o': 1, 'n': 1, ' ': 1, 'a': 1})
