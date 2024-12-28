# giong như list
# list là danh sách động, có thể thay đổi được
# tuple thì là danh sách ko thể thay đổi, giống như string
# khi dùng với các hàm như dict hay set yêu cầu đầu vào là các biến bất biến mà bạn đang cần lưu là 1 danh sách
# thì ta sẽ dùng tuple thay vì list

my_tuple = (1,2,3,4,4,4)
a = [1,2,'3']
my_tuple_1 = tuple(a)
print(my_tuple_1)
