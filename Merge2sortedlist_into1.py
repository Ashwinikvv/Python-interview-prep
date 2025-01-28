# https://algo.monster/liteproblems/88 for explanation 
'''Given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Merge B into A in sorted order.

Examples: 

Input : a[] = {10, 12, 13, 14, 18, NA, NA, NA, NA, NA}   
        b[] = {16, 17, 19, 20, 22};;
Output : a[] = {10, 12, 13, 14, 16, 17, 18, 19, 20, 22}
One way is to merge the two arrays by inserting the smaller elements in front of A, but the issue with this approach is that we have to shift every element to right after every insertion.
So, instead of comparing which one is a smaller element, we can compare which one is larger and then insert that element into the end of A.'''

# Python3 program to merge B 
# into A in sorted order
NA = -1

# Merging b[] into a[]
def sortedMerge(a, b, n, m):

	i = n - 1
	j = m - 1
	
	lastIndex = n + m - 1
	
	# Merge a and b, starting from last
	# element in each
	while (j >= 0) :
	
		# End of a is greater than end 
		# of b
		if (i >= 0 and a[i] > b[j]):
			
			# Copy Element
			a[lastIndex] = a[i] 
			i -= 1
		else:
			
			# Copy Element
			a[lastIndex] = b[j]
			j -= 1
		
		# Move indices
		lastIndex-= 1

# Helper function to print 
# the array
def printArray(arr, n):

	print("Array A after merging B in sorted order : ")

	for i in range(0, n):
		print(arr[i], end =" ")

size_a = 10

a = [10, 12, 13, 14, 18, NA, NA, NA, NA, NA]
n = 5

b = [16, 17, 19, 20, 22]
m = 5

sortedMerge(a, b, n, m)
printArray(a, size_a)

# This code is contributed by
# Smitha Dinesh Semwal
