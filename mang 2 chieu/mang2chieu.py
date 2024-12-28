# giai phap la dùng list chứa list
# tạo ra list độ dài n chứa các list_con có độ dài m (n hàng m cột):
n,m = 3,4
# khởi tạo ma trận a gồm n hàng m cột toàn số 00
a = [[0 for x in range(m)] for y in range(n)]   # đây là List Comprehension

# nhập ma trận
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

# duyệt các phần tử trong ma trận:
for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()