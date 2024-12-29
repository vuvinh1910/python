t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    ch = ord('A')
    while(k%2!=1):
        ch+=1
        k /= 2
    print(chr(ch))