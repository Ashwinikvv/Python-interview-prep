[Expected Approach] Using Sliding Window Technique – O(n) Time and O(1) Space
The idea is to use two pointers, start and end, to mark the start and end points of the current subarray (or window). Initially, both pointers are set at the beginning of the array. Continuously increase the size of the current window by incrementing the end pointer while keeping track of the count of zeros within the window. If at any point the count of zeros exceeds k, shrink the window by incrementing the start pointer until the count is reduced to k. The result will be the maximum length among all windows that contain at most k zeros.





# Python program to find the maximum subarray having 
# all ones, using sliding window technique

def maxOnes(arr, k):
    res = 0

    # Start and end pointer of the window
    start = 0
    end = 0

    # Counter to keep track of zeros in current window
    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1

        # Shrink the window from left if no. 
        # of zeroes are greater than k
        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))

        # Increment the end pointer 
        # to expand the window
        end += 1

    return res

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes(arr, k))

Output
8
