Longest Subarray with 0 Sum
Last Updated : 02 Nov, 2024
Given an array arr[] of size n, the task is to find the length of the longest subarray with sum equal to 0.

Examples:

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23}
Output: 5
Explanation: The longest subarray with sum equals to 0 is {-2, 2, -8, 1, 7}


Input: arr[] = {1, 2, 3}
Output: 0
Explanation: There is no subarray with 0 sum


Input:  arr[] = {1, 0, 3}
Output:  1
Explanation: The longest sub-array with sum equal to 0 is {0}


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Iterating over all subarrays – O(n^2) Time and O(1) Space
[Expected Approach] Using Hashmap and Prefix Sum – O(n) Time and O(n) Space
[Naive Approach] Iterating over all subarrays – O(n2) Time and O(1) Space:
Generate all sub-arrays one by one and check the sum of each subarray. If the sum of the current subarray is equal to zero then update the maximum length accordingly. After iterating over all the subarrays, return the maximum length.





# Function to find the length of the 
# largest subarray with sum 0
def max_len(arr):
    
    n = len(arr)
  
    # Initialize the result
    max_len = 0

    # Loop through each starting point
    for i in range(n):
      
        # Initialize the current sum for
        # this starting point
        curr_sum = 0

        # Try all subarrays starting from 'i'
        for j in range(i, n):
          
            # Add the current element to curr_sum
            curr_sum += arr[j]

            # If curr_sum becomes 0, update max_len if required
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)
    
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(max_len(arr))
