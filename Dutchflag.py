# Python program to sort an array of 0s, 1s and 2s 
# using Dutch National Flag Algorithm

# Function to sort an array of 0s, 1s and 2s
def sort012(arr):
    n = len(arr)
    lo = 0
    hi = n - 1
    mid = 0

    # Iterate till all the elements are sorted
    while mid <= hi:
      if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        lo = lo + 1
        mid = mid + 1
        
      elif arr[mid] == 1:
        mid = mid + 1
        
      else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi - 1
        
    return arr

arr = [0, 1, 2, 0, 1, 2]
arr = sort012(arr)

for x in arr:
    print(x, end=" ")


# Python Program to sort an array of 0s, 1s and 2s
# by counting the occurrence of 0s, 1s and 2s

# Function to sort an array of 0s, 1s and 2s
def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0

    # Count 0s, 1s and 2s
    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1

    idx = 0
    
    # Place all the 0s
    for i in range(c0):
        arr[idx] = 0
        idx += 1

    # Place all the 1s
    for i in range(c1):
        arr[idx] = 1
        idx += 1

    # Place all the 2s
    for i in range(c2):
        arr[idx] = 2
        idx += 1


arr = [0, 1, 2, 0, 1, 2]
sort012(arr)

for x in arr:
  print(x, end = " ")
