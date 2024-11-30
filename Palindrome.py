# Python program to check if the given string is a palindrome  
  
# Creating a string  
sequence = 'abjucujba'  
# Reversing the string  
reverse = sequence[::-1]  
  
# Checking if the string is a palindrome  
if reverse == sequence:  
    print("The sequence is a palindrome")  
else:  
    print("The sequence is not a palindrome")  
