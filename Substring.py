'''22. Can the String Be Split into Dictionary Words?
You are provided with a large string and a dictionary of the words. You have to find if the input string can be segmented into words using the dictionary or not.  
The solution is reasonably straightforward. You have to segment a large string at each point and check if the string can be segmented to the words in the dictionary.

Run the loop using the length of the large string.
We will create two substrings. 
The first substring will check each point in the large string from s[0:i]
If the first substring is not in the dictionary, it will return False.
If the first substring is in the dictionary, it will create the second substring using s[i:0].
If the second substring is in the dictionary or the second substring is of zero length, then return True. Recursively call can_segment_str() with the second substring and return True if it can be segmented. '''


def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        first_str = s[0:i]
        if first_str in dictionary:
            second_str = s[i:]
            if (
                not second_str
                or second_str in dictionary
                or can_segment_str(second_str, dictionary)
            ):
                return True
    return False


s = "datacamp"
dictionary = ["data", "camp", "cam", "lack"]
can_segment_string(s, dictionary)
# True
