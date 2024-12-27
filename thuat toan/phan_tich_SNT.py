import math

def SNT(n):
  for i in range(2,math.isqrf(n)+1):
    while(n%i==0):
      print(i,end="*")
      n = n//i
  if(n>1):
    print(n,end='')
    
a = 19843
SNT(a)
