string = 'Javatpoint'  
result=''  
for s in string:    
if s in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):       
s = ''    
result += s  
print("Required string without vowels is:", result)  
