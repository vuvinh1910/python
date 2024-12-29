temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def convert(he10,heb):
    str = ''
    while(he10!=0):
        a = he10%heb
        he10 //= heb
        str += temp[a]
    str = str[::-1]
    return str
t = int(input())
for _ in range(t):
    he10,heb = map(int,input().split())
    print(convert(he10,heb))