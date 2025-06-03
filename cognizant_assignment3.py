# ---------------------------------------
# Task 1 - Countdown Timer


# Ask the user for a starting number
start = int(input("Enter the starting number for countdown: "))

# Countdown using a while loop
while start > 0:
    print(start, end=" ")
    start -= 1

# Print final message after countdown ends
print("Blast off!")

print("\n")  # Add a blank line for separation


# ---------------------------------------
# Task 2 - Multiplication Table
# ---------------------------------------

# Ask the user to input a number
num = int(input("Enter a number to generate its multiplication table: "))

# Print multiplication table from 1 to 10 using a for loop
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n")  # Add a blank line for separation


# ---------------------------------------
# Task 3 - Factorial Calculator
# ---------------------------------------

# Ask the user to input a number
n = int(input("Enter a number to calculate its factorial: "))

# Initialize factorial result
factorial = 1

# Calculate factorial using a for loop
for i in range(1, n + 1):
    factorial *= i

# Print the result
print(f"The factorial of {n} is {factorial}.")
