Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Solution 2: Two Pointers
The problem is actually asking us to find the longest subarray that contains at most one 
0
. The remaining length after deleting one element from this subarray is the answer.

Therefore, we can use two pointers 
j
 and 
i
 to point to the left and right boundaries of the subarray, initially 
j
=
0
, 
i
=
0
. In addition, we use a variable 
c
n
t
 to record the number of $0$s in the subarray.

Next, we move the right pointer 
i
. If 
n
u
m
s
[
i
]
=
0
, then 
c
n
t
 is incremented by 
1
. When 
c
n
t
>
1
, we need to move the left pointer 
j
 until 
c
n
t
≤
1
. Then, we update the answer, i.e., 
a
n
s
=
max
(
a
n
s
,
i
−
j
)
. Continue to move the right pointer 
i
 until 
i
 reaches the end of the array.

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
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = j = 0
        for i, x in enumerate(nums):
            cnt += x ^ 1
            while cnt > 1:
                cnt -= nums[j] ^ 1
                j += 1
            ans = max(ans, i - j)
        return ans
