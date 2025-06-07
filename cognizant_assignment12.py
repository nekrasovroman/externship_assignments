import logging

# Step 4: Configure logging to write errors to a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

# Welcome message
print("Welcome to the Error-Free Calculator!")

# Program loop
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("> ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option. Please choose a number from 1 to 5.")
        continue

    # Step 2: Input validation for numeric inputs
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError as e:
        print("Invalid input! Please enter valid numbers.")
        logging.error(f"ValueError occurred: {e}")
        continue

    # Step 3: Perform operation with exception handling
    try:
        if choice == "1":
            result = num1 + num2
            print(f"Result: {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"Result: {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"Result: {result}")
        elif choice == "4":
            if num2 == 0:
                raise ZeroDivisionError("division by zero")
            result = num1 / num2
            print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.error(f"Unexpected error: {e}")
    finally:
        print("Operation complete.")
