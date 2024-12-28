import math

def SNT(n):
  for i in range(2,math.isqrt(n)+1):
    while(n%i==0):
      print(i,end="")
      n = n//i
      if(n>1):
        print(end='*')
      else:
        print(end='')
  if(n>1):
    print(n,end='')
    
a = 68
SNT(a)
