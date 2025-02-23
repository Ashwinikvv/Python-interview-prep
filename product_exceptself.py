Product of Array Except Self
Last Updated : 13 Jan, 2025
Given an array arr[] of n integers, construct a product array res[] (of the same size) such that res[i] is equal to the product of all the elements of arr[] except arr[i]. 

Example: 

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: 


For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: 


For i = 0, res[i] = 0.
For i = 1, res[i] = 12.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(n):
            for j in range(n):
                if i!=j:
                    res[i]=res[i]*nums[j]
        return res
obj=Solution()
print(obj.productExceptSelf([1,2,3,4]))









[Efficient Approach] Using Product Array – O(n) Time and O(1) Space
The idea is to handle two special cases of the input array: when it contains zero(s) and when it doesn’t.


If the array has no zeros, product of array at any index (excluding itself) can be calculated by dividing the total product of all elements by the current element. 


However, division by zero is undefined, so if there are zeros in the array, the logic changes. If there is exactly one zero, the product for that index will be the product of all other non-zero elements, while the elements in rest of the indices will be zero. 
If there are more than one zero, the product for all indices will be zero, since multiplying by zero results in zero.

[Better approach] Using Prefix and Suffix Array – O(n) Time and O(n) Space
The above approach can be optimized by avoiding the repetitive calculation of products of elements. The idea is to precompute the prefix and suffix products and store them in two arrays. Now we can find the product of array except i-th element, by using these precomputed arrays in constant time.


product of array except i-th element = prefProduct[i] * suffProduct[i]


prefProduct[i] stores product of all elements before i-th index in the array.
suffProduct[i] stores product of all elements after i-th index in the array.





# Function to calculate the product of all
# elements except the current element
def productExceptSelf(arr):
    n = len(arr)
    prefProduct = [1] * n
    suffProduct = [1] * n
    res = [0] * n

    # Construct the prefProduct array
    for i in range(1, n):
        prefProduct[i] = arr[i - 1] * prefProduct[i - 1]

    # Construct the suffProduct array
    for j in range(n - 2, -1, -1):
        suffProduct[j] = arr[j + 1] * suffProduct[j + 1]

    # Construct the result array using
    # prefProduct[] and suffProduct[]
    for i in range(n):
        res[i] = prefProduct[i] * suffProduct[i]

    return res

if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(res)

Output
180 600 360 300 900 

# Function to calculate the product of all elements 
# except the current element

def productExceptSelf(arr):
    zeros = 0
    idx = -1
    prod = 1

    # Count zeros and track the index of the zero
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= arr[i]

    res = [0] * len(arr)

    # If no zeros, calculate the product for all elements
    if zeros == 0:
        for i in range(len(arr)):
            res[i] = prod // arr[i]
    # If one zero, set product only at the zero's index
    elif zeros == 1:
        res[idx] = prod

    return res


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = productExceptSelf(arr)
    print(" ".join(map(str, res)))
