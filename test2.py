import datetime
import functools
import collections
# import intertools
import re
import math


t = int(input())
for _ in range(t):
    n,m = map(int,input().strip().split())
    mt = []
    for i in range(n):
        mt.append(list(map(int,input().strip().split())))
    mt_T = [[0 for i in range(n)] for j in range(m)]
    mt_temp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            mt_T[j][i] = mt[i][j]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                mt_temp[i][j] += (mt[i][k] * mt_T[k][j])
    for i in mt_temp:
        for j in i:
            print(j , end=' ')
        print()