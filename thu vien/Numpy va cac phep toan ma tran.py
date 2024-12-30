import numpy as np

mt = []
for i in range(4):
    mt.append([int(x) for x in input().split()])   # nhap ma tran mt

matrix_1 = np.array(mt)   # chuyen list 2 chieu sang mang trong numpy, tuy la array nhung no cung ho tro cac phep toan ma tran
matrix_2 = matrix_1.T  # .T la ma tran chuyen vi
# nhan 2 ma tran
print(matrix_1 @ matrix_2)  # yeu cau cot matrix_1 = hang matrix_2
# cong 2 ma tran
print(matrix_1 + matrix_2)  # yeu cau phai cung hang cung cot
# luy thua ma tran:
print(np.linalg.matrix_power(matrix_1 ,5))  # matrix mũ 5
# dinh thuc det cua ma tran
print(np.linalg.det(matrix_1))
# rank cua ma tran
print(np.linalg.matrix_rank(matrix_1))
# nghich dao ma tran matrix -1:
print(np.linalg.inv(matrix_1))

# duyet qua cac phan tu trong ma tran lop arrays
print()
matrix_1 = np.linalg.inv(matrix_1)
for i in matrix_1:
    for j in list(i):
        print(f'test{j:.2f}',end=' ')  # test lai kien thuc f-string va lam trong so float
    print()
