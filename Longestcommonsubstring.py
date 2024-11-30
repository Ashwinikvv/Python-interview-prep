'''Given two strings ‘s1‘ and ‘s2‘, find the length of the longest common substring. 

Example: 

Input: s1 = “GeeksforGeeks”, s2 = “GeeksQuiz” 
Output : 5 
Explanation:
The longest common substring is “Geeks” and is of length 5.


Input: s1 = “abcdxyz”, s2 = “xyzabcd” 
Output : 4
Explanation:
The longest common substring is “abcd” and is of length 4.


Input: s1 = “abc”, s2 = “” 
Output : 0.
'''

def maxCommStr(s1, s2):
    m = len(s1)
    n = len(s2)

    res = 0

    # Consider every pair of index and find the length
    # of the longest common substring beginning with
    # every pair. Finally return max of all maximums.
    for i in range(m):
        for j in range(n):
            curr = 0
            while (i + curr) < m and (j + curr) < n and s1[i + curr] == s2[j + curr]:
                curr += 1
            res = max(res, curr)

    return res


s1 = "geeksforgeeks"
s2 = "practicewritegeekscourses"
print(maxCommStr(s1, s2))
