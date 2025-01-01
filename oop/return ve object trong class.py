class PhanSo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def nhan(self,other):
        self.x *= other.x
        self.y *= other.y
        return xu_ly(self.x,self.y)  # doi ham xu ly ngoai class de tao 1 doi tuong phan so moi
    def __str__(self):
        return f"{self.x}/{self.y}"
    
def xu_ly(x,y):
    return PhanSo(x,y) # tra ve lop phan so moi

if __name__ == '__main__':
    ps = PhanSo(5,6)
    ps2 = PhanSo(8,5)
    res = ps.nhan(ps2)
    print(res)