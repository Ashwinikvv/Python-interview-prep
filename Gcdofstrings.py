# Python3 program for the above approach

# Function that finds gcd of 2 strings
def gcd(str1, str2):

	# If str1 length is less than
	# that of str2 then recur
	# with gcd(str2, str1)
	if(len(str1) < len(str2)):
		return gcd(str2, str1)
	
	# If str1 is not the
	# concatenation of str2
	elif(not str1.startswith(str2)):
		return ""
	elif(len(str2) == 0):
		
		# GCD string is found
		return str1
	else:
		
		# Cut off the common prefix
		# part of str1 & then recur
		return gcd(str1[len(str2):], str2)

# Function to find GCD of array of
# strings
def findGCD(arr, n):
	result = arr[0]

	for i in range(1, n):
		result = gcd(result, arr[i])
	
	# Return the GCD of strings
	return result

# Driver Code

# Given array of strings
arr = ["GFGGFG", "GFGGFG", "GFGGFGGFGGFG" ]
n = len(arr)

# Function Call
print(findGCD(arr, n))

# This code is contributed by avanitrachhadiya2155
