# Task 1
name = 'Roman'
age = 20
height = 6.0

print("Hello! My name is " + name + ". I'm " + str(age) + " years old and " + str(height) + " feet tall.")

# Task 2

# Choose two numbers
num1 = 8
num2 = 5

# Addition
print("The sum of", num1, "and", num2, "is", num1 + num2)

# Subtraction
print("The difference when", num2, "is subtracted from", num1, "is", num1 - num2)

# Multiplication
print("The product of", num1, "and", num2, "is", num1 * num2)

# Division
print("The result of dividing", num1, "by", num2, "is", num1 / num2)


# Task 3

# Ask the user to enter a number
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("This number is positive. Awesome!")
elif num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")