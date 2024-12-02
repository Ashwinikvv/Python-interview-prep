def is_palindrome(text):

  """Checks if a string is a palindrome (case-insensitive)."""

  text = text.lower().replace(" ", "")  # Remove spaces and convert to lowercase

  return text == text[::-1]

‍

# Example usage

text = "Race car"

if is_palindrome(text):

  print(f"{text} is a palindrome.")

else:

  print(f"{text} is not a palindrome.")
