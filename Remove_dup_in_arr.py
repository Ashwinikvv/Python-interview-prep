'''
Can you remove duplicates from a sorted array?
Given an integer sorted array in increasing order, remove the duplicate numbers such that each unique element appears only once. Make sure you keep the final order of the array the same.

It is impossible to change the length of the array in Python, so we will place the result in the first part of the array. After removing duplicates, we will have k elements, and the first k elements in the array should hold the results. 
Example 1: input array is [1,1,2,2], the function should return 2. 

Example 2: input array is [1,1,2,3,3], the function should return 3.

Solution:

Run the loop for the range of 1 to the size of the array.
Check if the previous number is unique or not. We are comparing previous elements with the current one.  
If it is unique, update the array using insertIndex, which is 1 at the start, and add +1 to the insertIndex. 
Return insertIndex as it is the k. 
This question is relatively straightforward once you know how. If you put more time into understanding the statement, you can easily come up with a solution. '''
def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
removeDuplicates(array_1)
# 4


array_2 = [1,1,3,4,5,6,6]
removeDuplicates(array_2)
# 5
