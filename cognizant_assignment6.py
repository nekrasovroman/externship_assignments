import string

while True:
    # Step 1: Ask the user for a password
    password = input("Enter a password: ")

    # Step 2: Initialize checks
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    long_enough = len(password) >= 8

    # Store feedback messages
    issues = []

    if not long_enough:
        issues.append("at least 8 characters")
    if not has_upper:
        issues.append("one uppercase letter")
    if not has_lower:
        issues.append("one lowercase letter")
    if not has_digit:
        issues.append("one digit")
    if not has_special:
        issues.append("one special character")

    # Step 3: Display result
    if not issues:
        print("Your password is strong! 💪")
        break
    else:
        print("Your password needs:", ", ".join(issues) + ".")
        print("Please try again.\n")

    # Bonus: Strength meter (score out of 10)
    score = 0
    if long_enough: score += 2
    if has_upper: score += 2
    if has_lower: score += 2
    if has_digit: score += 2
    if has_special: score += 2

    print(f"Password strength score: {score}/10\n")
