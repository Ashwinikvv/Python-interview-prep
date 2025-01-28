Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x]:
                ans.append(x)
                cnt[x] -= 1
        return ans

We can use a hash table 
cnt
 to count the occurrences of each element in the array 
nums1
. Then, we iterate through the array 
nums2
. If an element 
x
 is in 
cnt
 and the occurrence of 
x
 is greater than 
0
, we add 
x
 to the answer and then decrement the occurrence of 
x
 by one.

After the iteration is finished, we return the answer array.

The time complexity is 
O
(
m
+
n
)
, and the space complexity is 
O
(
m
)
. Here, 
m
 and 
n
 are the lengths of the arrays 
nums1
 and 
nums2
, respectively.
