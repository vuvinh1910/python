class HocSinh:
    i = 0
    def __init__(self,name,age,gpa):
        self.__name = name
        self.__age = age
        self.__gpa = gpa
        HocSinh.i += 1
        self.__stt = HocSinh.i
    
    # lt la less than
    def __lt__(self,other):
        if(self.__gpa == other.__gpa):
            return self.__stt > other.__stt
        return self.__gpa > other.__gpa
    
    def getGpa(self):
        return self.__gpa
    def getName(self):
        return self.__name
    def getStt(self):
        return self.__stt
    
    def __str__(self):
        return f"HS{self.__stt:03d} {self.__name} {self.__age} {self.__gpa}"
    
if __name__ == '__main__':
    lst = []
    hs1 = HocSinh('vinh',19,3)
    hs2 = HocSinh('anh',19,2)
    hs3 = HocSinh('nguyen',19,3)
    lst.append(hs1)
    lst.append(hs2)
    lst.append(hs3)

    # neu da co ham __lt__ thi dung sort
    lst.sort()

    # hoac dung sort voi key lamba
    lst.sort(key=lambda hocsinh : (hocsinh.getGpa() ,hocsinh.getStt()))
    for hs in lst:
        print(hs)