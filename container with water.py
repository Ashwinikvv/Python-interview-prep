Container with Most Water
Last Updated : 16 Jan, 2025
Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

Examples :  

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base = 2. Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6.


Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are distance 4 apart. So the size of the base = 4. Height of container = min(5, 3) = 3. So total area = 4 * 3 = 12.


Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 25.


Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Finding all possible boundaries – O(n^2) Time and O(1) Space
[Expected Approach] Using Two Pointers – O(n) Time and O(1) Space
[Naive Approach] Finding all possible boundaries – O(n^2) Time and O(1) Space
The idea is to iterate over all pair of lines in the array. For each line arr[i], consider it as the left boundary and then iterate over all subsequent lines arr[j] (j > i) to consider them as them as the right boundary. For each pair of boundaries, calculate the water that can be contained between them by the formula min(arr[i], arr[j]) * (j – i). The result will be the maximum amount of water found across all pairs.




# Python Program to find the maximum amount of water
# by iterating over all possible boundaries

def maxWater(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
          
            # Calculate the amount of water
            amount = min(arr[i], arr[j]) * (j - i)
          
            # Keep track of maximum amount of water
            res = max(amount, res)
    return res

if __name__ == "__main__":
    arr = [2, 1, 8, 6, 4, 6, 5, 5]
    print(maxWater(arr))

Output
25
Time Complexity: O(n^2)
Auxiliary Space: O(1)

[Expected Approach] Using Two Pointers – O(n) Time and O(1) Space
The idea is to maintain two pointers: left pointer at the beginning of the array and right pointer at the end of the array. These pointers act as the container’s sides so we can calculate the amount of water stored between them using the formula: min(arr[left], arr[right]) * (right – left). 


After calculating the amount of water for the given sides, we can have three cases:


arr[left] < arr[right]: This means that we have calculated the water stored for the container of height arr[left], so increment left by 1.
arr[left] >= arr[right]: This means that we have calculated the water stored for the container of height arr[right], so decrement right by 1.
Repeat the above process till left is less than right keeping track of the maximum water stored as the result.


Why are we moving the pointer which is pointing to the shorter line?

We are moving the pointer pointing to the shorter line to potentially find a taller line and increase the container’s height. Moving the pointer to the taller line would only reduce the width, but the height cannot increase because of the shorter line, thus decreasing the amount of water.

Container-with-Most-Water-4.webpContainer-with-Most-Water-4.webp





# Python Program to find the maximum amount of water in the 
# container using Two Pointer Technique

def maxWater(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        
        # Find the water stored in the container between 
        # arr[left] and arr[right]
        water = min(arr[left], arr[right]) * (right - left)
        res = max(res, water)
        
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return res

  
if __name__ == "__main__":
    arr = [2, 1, 8, 6, 4, 6, 5, 5]
    print(maxWater(arr))

Output
25
