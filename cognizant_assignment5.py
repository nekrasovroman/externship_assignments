# ---------------------------------------
# Task 1 - String Slicing and Indexing
# ---------------------------------------

text = "Python is amazing!"

# Extracting slices
first_word = text[:6]
amazing_part = text[10:17]
reversed_text = text[::-1]

# Print the results
print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_text)

print("\n")  # Add a blank line for separation


# ---------------------------------------
# Task 2 - String Methods
# ---------------------------------------

s = " hello, python world! "

# Apply and print each string method
print("Original string:", repr(s))
print("After strip():", s.strip())
print("After capitalize():", s.strip().capitalize())
print("After replace():", s.strip().replace("world", "universe"))
print("After upper():", s.strip().upper())

print("\n")  # Add a blank line for separation


# ---------------------------------------
# Task 3 - Check for Palindromes
# ---------------------------------------

# Ask the user to enter a word
word = input("Enter a word: ")

# Check if it's a palindrome
if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome.")
