Solution 1: Sliding Window
First, we count the number of vowels in the first 
k
 characters, denoted as 
c
n
t
, and initialize the answer 
a
n
s
 as 
c
n
t
.

Then we start traversing the string from 
k
. For each iteration, we add the current character to the window. If the current character is a vowel, we increment 
c
n
t
. We remove the first character from the window. If the removed character is a vowel, we decrement 
c
n
t
. Then, we update the answer 
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
c
n
t
)
.

After the traversal, we return the answer.

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
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        ans = cnt = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels) - int(s[i - k] in vowels)
            ans = max(ans, cnt)
        return ans
