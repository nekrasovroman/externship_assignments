import turtle

# -----------------------------
# Recursive Factorial Function
# -----------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -----------------------------
# Recursive Fibonacci Function
# -----------------------------
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# -----------------------------
# Recursive Fractal Tree (Bonus)
# -----------------------------
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)


# -----------------------------
# Main Program Loop
# -----------------------------
def main():
    print("Welcome to the Recursive Artistry Program!")

    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            num = input("Enter a non-negative integer to find its factorial: ")
            if num.isdigit():
                num = int(num)
                print(f"The factorial of {num} is {factorial(num)}.")
            else:
                print("Invalid input. Please enter a non-negative integer.")

        elif choice == "2":
            num = input("Enter the position of the Fibonacci number (0 or greater): ")
            if num.isdigit():
                num = int(num)
                print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
            else:
                print("Invalid input. Please enter a non-negative integer.")

        elif choice == "3":
            print("Drawing a fractal tree...")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.left(90)
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()
