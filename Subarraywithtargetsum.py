def subarray_sum(arr, n, target_sum):

    # To store the result
    res = []

    # Flag to indicate if the subarray is found
    flag = False

    for i in range(n):
        current_sum = arr[i]  # Initialize the current sum

        # Check if the single element is the sum
        if current_sum == target_sum:
            res.append(i + 1)
            res.append(i + 1)
            flag = True
            break
        else:
            # Try all subarrays starting with 'i'
            for j in range(i + 1, n):
                current_sum += arr[j]

                if current_sum == target_sum:
                    res.append(i + 1)
                    res.append(j + 1)
                    flag = True
                    break
            if flag:
                break
    if flag:
        return res
    return [-1]  # If no subarray is found


# Driver Code
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    target_sum = 23
    result = subarray_sum(arr, n, target_sum)
    for i in result:
        print(i, end=" ")
