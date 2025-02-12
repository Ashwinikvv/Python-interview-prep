The idea is to use two pointers, one pointer will start from start of s1 and another will start from start of s2. If current character on both the indexes are same then increment both pointers otherwise increment the pointer which is pointing s2.

Follow the steps below to solve the problem:

Initialize the pointers i and j with zero, where i is the pointer to s1 and j is the pointer to s2.
If s1[i] = s2[j] then increment both i and j by 1.
Otherwise, increment only j by 1.
If i reaches the end of s1 then return TRUE else return FALSE.
Below is the implementation of the above approach

Check if one string is subsequence of other
Last Updated : 10 Feb, 2025
Given two strings s1 and s2, find if the first string is a Subsequence of the second string, i.e. if s1 is a subsequence of s2.  A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Examples : 

Input: s1 = “AXY”, s2 = “ADXCPY”
Output: True 
All characters of s1 are in s2 in the same order


Input: s1 = “AXY”, s2 = “YADXCP”
Output: False 
All characters are present, but order is not same.


Input: s1 = “gksrek”, s2 = “geeksforgeeks”
Output: True

# Iterative JavaScript program to check
# If a string is subsequence of another string

# Returns true if s1 is subsequence of s2


def issubsequence(s1, s2):

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n


# driver code
s1 = "gksrek"
s2 = "geeksforgeeks"
if (issubsequence(s1, s2)):
    print("gksrek is subsequence of geekforgeeks")
else:
    print("gksrek is not a subsequence of geekforgeeks")
