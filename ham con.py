def ten_ham(tham_so):
    # Các câu lệnh trong hàm
    print(tham_so)
ten_ham("haha") # gọi hàm ten_ham với haha truyền vào tham_so và thực hiện print trong hàm định nghia

#vidu:
def greet(name):
    print("Hello, " + str(name))
greet("Alice")  # Truyền vào một chuỗi kq: Hello, Alice
greet(42)       # Truyền vào một số nguyên nhưng sẽ sai cần phải đổi thành "hello, " + str(name) hoặc {name}
                # kq: Hello, 42

def greet(name):
    print(1+name)
greet(42)       # Truyền vào một số nguyên, kq: 43

def default_value(a,b = 'test'):
    print(a)
    return
default_value(1) # ko gan b thi mac dinh b = test
default_value(1,'hehe') # b = hehe
