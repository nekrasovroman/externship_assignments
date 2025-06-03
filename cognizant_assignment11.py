# ----------------------------------------
# Task 1 - Understanding Python Exceptions
# ----------------------------------------

while True:
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result}.")
        break  # Exit loop if successful
print("\n")


# ----------------------------------------
# Task 2 - Types of Exceptions
# ----------------------------------------

# IndexError: happens when accessing an index that doesn't exist
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Invalid index
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError: occurs when accessing a dictionary with a non-existent key
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["z"])  # Key "z" doesn't exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError: happens when using unsupported operand types
try:
    result = "5" + 3  # Can't add str and int
except TypeError:
    print("TypeError occurred! Unsupported operand types.")
print("\n")


# -----------------------------------------------------
# Task 3 - Using try...except...else...finally
# -----------------------------------------------------

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter numbers only.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
