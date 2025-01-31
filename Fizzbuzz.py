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

    return res

if __name__ == "__main__":
    n = 20
    res = fizzBuzz(n)

    for s in res:
        print(s, end=" ")
