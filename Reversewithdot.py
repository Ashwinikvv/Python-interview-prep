
# Python program to reverse words in a string
'''Given a string str, the task is to reverse the order of the words in the given string. Note that str may contain leading or trailing dots(.) or multiple trailing dots(.) between two words. The returned string should only have a single dot(.) separating the words.

Examples:

Input: str = “i.like.this.program.very.much” 
Output: str = “much.very.program.this.like.i” 


Input: str = ”..geeks..for.geeks.” 
Output: str = “geeks.for.geeks”'''

def reverse_words(str):
    
    # Split the input string by '.' while 
    # ignoring multiple consecutive dots
    words = [word for word in str.split('.') if word]
    
    # Reverse the words
    words.reverse()
    
    # Join the reversed words back into a string
    return '.'.join(words)


if __name__ == "__main__":
    str = "..geeks..for.geeks."
    print(reverse_words(str))
