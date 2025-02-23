Given, an array of size n. Find an element that divides the array into two sub-arrays with equal sums.

Examples: 


Input: 1 4 2 5 0
Output: 2
Explanation: If 2 is the partition, subarrays are : [1, 4] and [5]


Input: 2 3 4 1 4 5
Output: 1
Explanation: If 1 is the partition, Subarrays are : [2, 3, 4] and [4, 5]


Input: 1 2 3
Output: -1
Explanation: No sub-arrays possible. return -1

# Python 3 Program to find an element
# such that sum of right side element
# is equal to sum of left side

# Function to Find an element in
# an array such that left and right
# side sums are equal


def findElement(arr, n):
	for i in range(1, n):
		leftSum = sum(arr[0:i])
		rightSum = sum(arr[i+1:])
		if(leftSum == rightSum):
			return arr[i]
	return -1


# Driver Code
if __name__ == "__main__":

	# Case 1
	arr = [1, 4, 2, 5]
	n = len(arr)
	print(findElement(arr, n))

	# Case 2
	arr = [2, 3, 4, 1, 4, 5]
	n = len(arr)
	print(findElement(arr, n))



prefix and suffix arrays

# Python 3 Program to find an element 
# such that sum of right side element 
# is equal to sum of left side

# Function for Finds an element in 
# an array such that left and right
# side sums are equal 
def findElement(arr, n) :
	
	# Forming prefix sum array from 0 
	prefixSum = [0] * n
	prefixSum[0] = arr[0]
	for i in range(1, n) :
		prefixSum[i] = prefixSum[i - 1] + arr[i]

	# Forming suffix sum array from n-1
	suffixSum = [0] * n
	suffixSum[n - 1] = arr[n - 1]
	for i in range(n - 2, -1, -1) :
		suffixSum[i] = suffixSum[i + 1] + arr[i]

	# Find the point where prefix 
	# and suffix sums are same.
	for i in range(1, n - 1, 1) :
		if prefixSum[i] == suffixSum[i] :
			return arr[i]
		
	return -1

# Driver Code
if __name__ == "__main__" :
	
	arr = [ 1, 4, 2, 5]
	n = len(arr)
	print(findElement(arr, n))

# This code is contributed by ANKITRAI1

We form a prefix and suffix sum arrays

Given array: 1 4 2 5
Prefix Sum:  1  5 7 12
Suffix Sum:  12 11 7 5

Now, we will traverse both prefix arrays.
The index at which they yield equal result,
is the index where the array is partitioned 
with equal sum.
