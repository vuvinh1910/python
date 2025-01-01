
class NhanVien:
    stt = 0     # day la bien static cho tat ca NhanVien

    # init() la ham se duoc goi moi khi class nhanvien duoc tao, init() la ham khoi tao cua nhan vien
    def __init__(self,name,age,money):  # self la ham mac dinh luon luon phai co, cac tham so sau self la cac field dau vao
        self.name1 = name # PUBLIC
        self.__name2 = name # PRIVATE, ta nen dung pham vi private de dam bao tinh dong goi

        self.__name = name  # self.field la khoi tao cac field tu self
        self.__age = age
        self.__money = money
        NhanVien.stt += 1  # tang so luong nhan vien len 1, bang cach tham chieu den bien static stt
        self.__code = NhanVien.stt
        # stt += 1    cai nay se sai vi stt la bien toan class nhung khong phai bien duoc khai bao trong init() nen ko truy cap dc

    # custom method, ham tu tao
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getMoney(self):
        return self.__money
    
    def setName(self,new_name):
        self.__name = new_name

    # giong nhu ham soString ben java
    def __str__(self):
        return f"NV{self.__code:03d} {self.__name} {self.__age} {self.__money}"
    
if __name__ == '__main__':
    nhanvien1 = NhanVien('le ving',20,100000)
    nhanvien2 = NhanVien('le quan',20,200000)
    print(nhanvien1)
    print(nhanvien2)