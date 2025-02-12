3 Sum – All Distinct Triplets with given Sum in an Array
Last Updated : 08 Jan, 2025
Given an array arr[], and an integer target, find all possible unique triplets in the array whose sum is equal to the given target value. We can return triplets in any order, but all the returned triplets should be internally sorted, i.e., for any triplet [q1, q2, q3], the condition q1 ≤ q2 ≤ q3 should hold.

Examples: 

Input: arr[] = {12, 3, 6, 1, 6, 9}, target = 24 
Output: {{3, 9, 12}, {6, 6, 12}} 
Explanation: There are two unique triplets that add up to 24: 
3 + 9 + 12 = 24
6 + 6 + 12 = 24

Input: arr[] = {-2, 0, 1, 1, 2}, target = 10 
Output: {} 
Explanation: There is not triplet with sum 10.


Table of Content

[Naive Approach] – By Exploring all the triplets – O(n^4) Time and O(1) Space
[Better Approach] – Using Hashing – O(n^2) Time and O(n) Space
[Expected Approach] – Using Two Pointers Technique – O(n^2) Time and O(1) Space
[Naive Approach] – By Exploring all the triplets – O(n^4) Time and O(1) Space
We use three nested loops to generate all possible triplets, then check if their sum is equal to the target. If it is, we run an additional loop to check if the triplet is already in the result; if not, we add it.




# Python program to find all the distinct triplets having sum
# equal to given target by exploring all the triplets

def threeSum(arr, target):
    res = []
    n = len(arr)

    # Generating all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    curr = sorted([arr[i], arr[j], arr[k]])

                    # If triplet doesn't exist in the res, then only insert it.
                    if curr not in res:
                        res.append(curr)
    return res

if __name__ == "__main__":
    arr = [12, 3, 6, 1, 6, 9]
    target = 24

    ans = threeSum(arr, target)
    for triplet in ans:
        print(triplet[0], triplet[1], triplet[2])

Output
3 9 12
6 6 12
[Better Approach] – Using Hashing – O(n^2 log n) Time and O(n) Space
The idea is to maintain a hash set to track whether a particular element occurred in the array so far or not. As we traverse all pairs using two nested loops, for each pair {arr[i], arr[j]}, we check if the complement (target - arr[i] - arr[j]) is already in the set. If it is, we have found a triplet whose sum equals the target. Each valid triplet is inserted into ta hash set to avoid duplicates.




# Python program to find all unique triplets having sum
# equal to target using hashing

def threeSum(arr, target):
    n = len(arr)
    
    # Set to handle duplicates
    resSet = set()
    
    # Generating all pairs
    for i in range(n):
        s = set()
        for j in range(i + 1, n):
            complement = target - arr[i] - arr[j]
            
            # If the complement exists in the hash set then we 
            # have found the triplet with sum, target
            if complement in s:
                curr = tuple(sorted([arr[i], arr[j], complement]))
                resSet.add(curr)
                
            s.add(arr[j])
    
    return list(resSet)

if __name__ == "__main__":
    arr = [12, 3, 6, 1, 6, 9]
    target = 24
    
    ans = threeSum(arr, target)
    for triplet in ans:
        print(triplet[0], triplet[1], triplet[2])

Output
3 9 12
6 6 12
[Expected Approach] – Using Two Pointers Technique – O(n^2) Time and O(1) Space
The idea is to sort the array and use two pointers technique to find all the triplets. We will traverse the array and fix the first element of the triplet then, Initialize two pointers at the beginning and end of the remaining array. Now, compare the sum of elements at these pointers: 


If sum = target, store the triplet and skip duplicates to ensure they are distinct. 
If sum < target, we move the left pointer towards right. 
If sum > target, we move the right pointer towards left. 



# Python program to find all the distinct triplets having sum
# equal to target using two pointer technique

def three_sum(arr, target):
    res = []
    n = len(arr)

    arr.sort()

    for i in range(n):
      
        # Skip duplicates for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Two pointer technique
        j, k = i + 1, n - 1
        while j < k:
            sum_value = arr[i] + arr[j] + arr[k]
            if sum_value == target:
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1

                # Skip duplicates for j and k
                while j < n and arr[j] == arr[j - 1]:
                    j += 1
                while k > j and arr[k] == arr[k + 1]:
                    k -= 1
            elif sum_value < target:
                j += 1
            else:
                k -= 1
    return res

arr = [12, 3, 6, 1, 6, 9]
target = 24

ans = three_sum(arr, target)
for triplet in ans:
    print(f"{triplet[0]} {triplet[1]} {triplet[2]}")
Try it on GfG Practice
redirect icon

Output
3 9 12
6 6 12
