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


# if else lồng nhau
a, b = 10, 20
if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")


# ham con ket hop tra ve 
def condition1(age):
  return(age >= 5)
  
age = int(input())
if condition1(age):
    print("Your cat is old")
else:
    print("Your cat is young")
