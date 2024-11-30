'''Can you find the missing number in the array?
You have been provided with the list of positive integers from 1 to n. All the numbers from 1 to n are present except x, and you must find x. n = 8 
arr=[3,5,4,2,1,6,8]
missing number = 7
This question is a simple math problem.

Find the sum of all elements in the list.
By using arithmetic series sum formula, we will find the expected sum of the first n numbers. 
Return the difference between the expected sum and the sum of the elements.  '''
def find_missing(input_list):

  sum_of_elements = sum(input_list)
 
  # There is exactly 1 number missing
  n = len(input_list) + 1
  actual_sum = (n * ( n + 1 ) ) / 2
 
  return int(actual_sum - sum_of_elements)
list_1 = [1,5,6,3,4]


find_missing(list_1)
# 2
