Alternatively Merge two Strings
Last Updated : 23 Feb, 2023
Given 2 strings, merge them in an alternate way, i.e. the final string’s first character is the first character of the first string, the second character of the final string is the first character of the second string and so on. And if once you reach end of one string while if another string is still remaining then append the remaining of that string to final string 

Examples: 

Input : string 1 :"geeks"
        string 2 :"forgeeks"
Output: "gfeoerkgseeks"
Explanation : The answer contains characters from alternate strings, and once 
the first string ends the remaining of the second string is added to the final string

Input :string 1 :"hello"
        string 2 :"geeks"
Output : hgeelelko


# Python3 code to alternatively merge two strings 

# Function for alternatively merging two strings 
def merge(s1, s2): 
	
	# To store the final string 
	result = "" 

	# For every index in the strings 
	i = 0
	while (i < len(s1)) or (i < len(s2)): 
		
		# First choose the ith character of the 
		# first string if it exists 
		if (i < len(s1)): 
			result += s1[i] 

		# Then choose the ith character of the 
		# second string if it exists 
		if (i < len(s2)): 
			result += s2[i] 
			
		i += 1
		
	return result 

# Driver Code 
s1 = "geeks"
s2 = "forgeeks"

print(merge(s1, s2)) 

# This code is contributed by divyesh072019
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
