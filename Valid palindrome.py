We use two pointers 
i
 and 
j
 to point to the two ends of the string 
s
, and then loop through the following process until 
i
≥
j
:

If 
s
[
i
]
 is not a letter or a number, move the pointer 
i
 one step to the right and continue to the next loop.
If 
s
[
j
]
 is not a letter or a number, move the pointer 
j
 one step to the left and continue to the next loop.
If the lowercase form of 
s
[
i
]
 and 
s
[
j
]
 are not equal, return false.
Otherwise, move the pointer 
i
 one step to the right and the pointer 
j
 one step to the left, and continue to the next loop.
At the end of the loop, return true.

The time complexity is 
O
(
n
)
, where 
n
 is the length of the string 
s
. The space complexity is 
O
(
1
)
.

Python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i + 1, j - 1
        return True
