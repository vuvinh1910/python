temperature = int(input())
if temperature >= 100:
    print("Stay at home and enjoy a good movie")
elif temperature >= 92:
    print("Stay at home")
elif temperature == 75:
    print("Go outside and enjoy the weather")
elif temperature < 0:
    print("It's cool outside")
else:
    print("Let's go to school")
# elif chinh la else ket hop voi if


n = int(input())
if n % 2 == 0:
    # Nếu n là số chẵn thì hiển thị ra màn hình n is an even number
    print("n is an even number")
else:
    # Ngược lại, nếu n không là số chẵn thì hiển thị ra màn hình n is an odd number
    print("n is an odd number")


# if else nhieu dieu kien
a,b = 4,5
if a%2==0 and b>a:
    print(1)
else :
    print(0)


# ham con ket hop tra ve 
def condition1(age):
  return(age >= 5)
  
age = int(input())
if condition1(age):
    print("Your cat is old")
else:
    print("Your cat is young")
