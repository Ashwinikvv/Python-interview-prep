You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
<ul>



Return the array formed after rearranging the values of nums.

 

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
Example 2:

Input: nums = [2,1]
Output: [2,1]
Explanation: 
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array. 
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
Solutions


Solution 1: Sorting
We can extract the elements at odd and even indices separately, then sort the array of odd indices in non-increasing order and the array of even indices in non-decreasing order. Finally, merge the two arrays back together.

The time complexity is 
O
(
n
log
⁡
n
)
, and the space complexity is 
O
(
n
)
. Here, 
n
 is the length of the array 
nums
.

Python3
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = sorted(nums[::2])
        b = sorted(nums[1::2], reverse=True)
        nums[::2] = a
        nums[1::2] = b
        return nums
