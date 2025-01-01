                        # tieng viet co dau
f = open("text.txt","r",encoding="UTF8")
# print(f.read())  in ra toan bo noi dung trong file
# print(f.readline(),end='')  in ra dong dau tien, end='' vi trong file da co ky tu enter

for line in f:      # f cung chua cac dong, co the duyet cac dong trong file qua vong for
    print(line,end='')

# neu mode la a (append) thi se giu lai noi dung va lam viec tu dong cuoi cung
f2 = open("output.txt",'w') # neu chua co thi tu dong tao moi file, neu da ton tai file thi xoa toan bo noi dung va lam viec tu dong dau tien
f2.write('concac\n')