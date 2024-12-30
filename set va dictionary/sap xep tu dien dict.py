import functools 

# key la ten, value la (diem,so_lan_nop_bai)
# ham custom so sanh key va value
def sx(a,b):
    if(a[1][0] == b[1][0] and a[1][1] == b[1][1]): # neu bang ca diem va so lan nop bai
        return ord(a[0][0]) - ord(b[0][0])  # so sanh ten theo tu dien, chu cai dau tien
    elif(a[1][0] == b[1][0]):
        return a[1][1] - b[1][1]  # neu cung diem thi so sanh so lan nop bai it hon
    return  - (a[1][0] - b[1][0]) # neu it diem hon thi sx giam dan


t = int(input())
my_dick = dict()
for i in range(t):
    name = input()
    tup = tuple([int(x) for x in input().split()])   # dict chi nhan cac tham so bat bien nen dung tuple thay list
    my_dick[name] = tup

                # .items() de lay ca key-value de truyen vao a,b trong ham sx()
my_dick = sorted(my_dick.items(),key=functools.cmp_to_key(sx))

# sau khi dung sorted thi my_dick chuyen thanh list nen ta duyet ko can .items()
for k,v in my_dick:
    print(k,end=' ')
    print(v[0],v[1])