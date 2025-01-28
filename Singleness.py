Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

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
