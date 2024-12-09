# Python program to reverse words in a string

def reverse_words(str):
    stack = []
    word = ""

    # Iterate through the string
    for ch in str:
        
        # If not a dot, build the current word
        if ch != '.':
            word += ch
        
        # If we see a dot, push the word into the stack
        elif word:
            stack.append(word)
            word = ""

    # Last word remaining, push it to stack
    
    print(stack)
    # Rebuild the string from the stack
    return ".".join(stack[::-1])

if __name__ == "__main__":
    str = "..geeks..for.geeks."
    print(reverse_words(str))
