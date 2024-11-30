# Python program to check if a number is prime or not  
  
# Declaring a variable  
n = 37  
if n == 2:  
    print("2 is a prime number")  
  
if n != 1:  
    for i in range(2, n):  
        if n % i == 0:  
            print("The given number is a composite number")  
            break  
        if i == n-1:  
            print("The given number is a prime number")  
else:  
    print("1 is not a prime number")  
