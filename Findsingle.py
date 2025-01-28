def find_single(arr):
    freq = {}

    # Store the frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find and return the element that appears only once
    for key, value in freq.items():
        if value == 1:
            return key

    # If no single element is found, return -1
    return -1

if __name__ == '__main__':
    arr = [2, 3, 5, 4, 5, 3, 4]
    print(find_single(arr))
Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.

Example : 

Input:  arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2 


Input:  arr[] = {2, 5, 2}
Output: 5


Input:  arr[] = {3}
Output: 3



