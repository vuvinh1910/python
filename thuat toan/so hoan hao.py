# la so ma co cac uoc nho hon no cong lai = chinh no
import math

def perfect(n):
  tong = 1
  for i in range(2,math.isqrt(n)+1):
    if(n%i==0):
      tong += i
      if(i != n/i):
        tong += n/i
  return tong == n

a=496
print(perfect(a))
