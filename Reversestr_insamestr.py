Solution 1: Two Pointers
We use two pointers 
i
 and 
j
, initially pointing to the start and end of the array respectively. Each time, we swap the elements at 
i
 and 
j
, then move 
i
 forward and 
j
 backward, until 
i
 and 
j
 meet.

The time complexity is 
O
(
n
)
, where 
n
 is the length of the array. The space complexity is 
O
(
1
)
.

Python3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
