You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Solution 1: Sliding Window
We maintain a sliding window of length 
k
, and for each window, we calculate the sum 
s
 of the numbers within the window. We take the maximum sum 
s
 as the answer.

The time complexity is 
O
(
n
)
, where 
n
 is the length of the array 
n
u
m
s
. The space complexity is 
O
(
1
)
.

Python3
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = s = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)
        return ans / k
