class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary mapping Roman numerals to integers.
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      
        # Initialize the previous number with the value of the last Roman numeral.
        previous_number = roman_to_int[s[-1]]
      
        # Initialize the total with the value of the last Roman numeral.
        total = previous_number
      
        # Loop over the string of Roman numerals in reverse order (right-to-left).
        for i in range(len(s) - 2, -1, -1):
            # Get the integer value of the current Roman numeral.
            current_number = roman_to_int[s[i]]
          
            # If the current value is less than the previous value, we need to subtract it.
            # Otherwise, we add it.
            if current_number < previous_number:
                total -= current_number
            else:
                total += current_number
          
            # Update the previous number for the next iteration.
            previous_number = current_number
      
        # Return the computed total, which is the integer equivalent of the Roman numeral string.
        return total

# Example use:Example use:
# solution = Solution()
# result = solution.romanToInt("MCMXCIV")
# print(result)  # Output: 1994
