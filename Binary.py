num = 1101001  
while(num > 0):  
    l = num % 10  
     
if l!=0 and l!=1:  
         
print("given number is not binary")  
         
break  
     
num = num // 10  
     
if num == 0:  
         
print("given number is binary")  
