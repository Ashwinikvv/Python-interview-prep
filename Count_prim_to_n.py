# Function to count prime numbers up to a given limit 'n'
def count_Primes_nums(n):
    ctr = 0  # Counter to store the number of prime numbers
    
    # Iterate through numbers up to 'n'
    for num in range(n):
        if num <= 1:  # Numbers less than or equal to 1 are not prime, so skip them
            continue
        
        # Check for factors in the range from 2 to num-1
        for i in range(2, num):
            if (num % i) == 0:  # If num is divisible by i, it's not prime
                break
        else:
            ctr += 1  # If no factors are found, increment the counter (num is prime)

    return ctr  # Return the count of prime numbers

# Print the count of prime numbers up to 10 and 100
print(count_Primes_nums(10))
print(count_Primes_nums(100))
