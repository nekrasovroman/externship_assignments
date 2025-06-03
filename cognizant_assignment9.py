# -----------------------------------------
# Task 1 - Writing Functions
# -----------------------------------------

def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

# Example usage
greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")

print("\n")


# -----------------------------------------
# Task 2 - Using Default Parameters
# -----------------------------------------

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage
describe_pet("Buddy")             # Uses default value "dog"
describe_pet("Whiskers", "cat")   # Overrides with "cat"

print("\n")


# -----------------------------------------
# Task 3 - Functions with Variable Arguments
# -----------------------------------------

def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

# Example usage
make_sandwich("Lettuce", "Tomato", "Cheese")

print("\n")


# -----------------------------------------
# Task 4 - Understanding Recursion
# -----------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")
