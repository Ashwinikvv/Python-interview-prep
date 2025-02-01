
def reverse_digits(num):
    # Initialize reverse number as 0
    rev = 0

    # Check sign of the number
    sign = -1 if num < 0 else 1

    # Take absolute value of the number
    num = abs(num)

    # Reverse the digits
    while num != 0:
        # Get the last digit
        rem = num % 10

        # Remove the last digit from the number
        num = num // 10

        # Check if the reverse number will overflow 32-bit integer
        if rev > 2**31//10 or (rev == 2**31//10 and rem > 7):
            return 0

        # Check if the reverse number will underflow 32-bit integer
        if rev < -2**31//10 or (rev == -2**31//10 and rem < -8):
            return 0

        # Update the reverse number
        rev = rev * 10 + rem

    # Return the reverse number with the original sign
    return sign * rev

if __name__ == '__main__':
    num = 12345
    print("Reverse of no. is", reverse_digits(num))

    num = 1000000045
    print("Reverse of no. is", reverse_digits(num))


The above approach won’t work if we are given a signed 32-bit integer x, and return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 – 1], then return 0. So we cannot multiply the number*10 and then check if the number overflows or not.


We must check the overflow condition before multiplying by 10 by using the following logic :
You are checking the boundary case before you do the operation. (reversed >INT_MAX ) wouldn’t work because reversed will overflow and become negative if it goes past MAX_VALUE.  Dividing MAX_VALUE by 10 lets you check the condition without overflowing INT_MAX is equal 2147483647. INT_MIN is equal  -2147483648.  The last digits are 7 and 8. This is the reason why we also  check  rem > 7 and rem < -8 conditions
