  Longest Common Prefix

Solution
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


# Python program to find the longest common prefix
# using Character by Character Matching

# Function to find the longest common prefix
# from the list of strings
def longestCommonPrefix(arr):
  
      # Find length of smallest string
    minLen = len(arr[0])

    for s in arr:
        minLen = min(minLen, len(s))

    res = []
    for i in range(minLen):

        # Current character (must be the same
        # in all strings to be a part of result)
        ch = arr[0][i]

        for s in arr:
            if s[i] != ch:
                return "".join(res)

        # Append to result
        res.append(ch)


sorting approach

# Python 3 program to find longest 
# common prefix of given array of words.
def longestCommonPrefix( a):
	
	size = len(a)

	# if size is 0, return empty string 
	if (size == 0):
		return ""

	if (size == 1):
		return a[0]

	# sort the array of strings 
	a.sort()
	
	# find the minimum length from 
	# first and last string 
	end = min(len(a[0]), len(a[size - 1]))

	# find the common prefix between 
	# the first and last string 
	i = 0
	while (i < end and
		a[0][i] == a[size - 1][i]):
		i += 1

	pre = a[0][0: i]
	return pre

# Driver Code
if __name__ == "__main__":

	input = ["geeksforgeeks", "geeks", 
					"geek", "geezer"]
	print("The longest Common Prefix is :" ,
				longestCommonPrefix(input))

# This code is contributed by ita_c

    return "".join(res)

if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))


