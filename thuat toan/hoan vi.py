import itertools

s=[9,3,4,6,7]
s.sort()
per = itertools.permutations(s)
for i in per:
    print(" ".join(map(str,i)))
