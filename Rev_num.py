'''Reverse a number '''
n = int(input("Enter number: "))  
  
reverse = 0  
  
while(n>0):  
    digit = n%10  
    reverse = reverse*10+digit  
    n=n//10  
print("The reverse of the number:",reverse)  
