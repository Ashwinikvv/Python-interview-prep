# Python Code to check if two Strings are anagram of 
# each other using Dictionary

def areAnagrams(s1, s2):
    
    # Create a hashmap to store character frequencies
    charCount = {}
    
    # Count frequency of each character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
  
    # Count frequency of each character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
  
    # Check if all frequencies are zero
    for value in charCount.values():
        if value != 0:
            return False
    
    # If all conditions satisfied, they are anagrams
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")



# Python Code to check if two Strings are anagram of 
# each other using sorting

def areAnagrams(s1, s2):
    
    # Sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare sorted strings
    return s1 == s2

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")
