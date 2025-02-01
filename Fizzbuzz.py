# Python program for Fizz Buzz Problem 
# by checking every integer individually 
# with hashing

def fizzBuzz(n):
    res = []  

    # Dictionary to store all FizzBuzz mappings.
    mp = {3: "Fizz", 5: "Buzz"}
    divisors = [3, 5] 

    for i in range(1, n + 1):
        s = ""  

        for d in divisors: 
          
            # If the i is divisible by d, add the 
              # corresponding string mapped with d
            if i % d == 0:
                s += mp[d]

        # Not divisible by 3 or 5, add the number
        if not s:
            s += str(i)

        # Append the current answer str to the result list
        res.append(s)


    Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

    return res

if __name__ == "__main__":
    n = 20
    res = fizzBuzz(n)

    for s in res:
        print(s, end=" ")
