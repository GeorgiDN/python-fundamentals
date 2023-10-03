def validate_password(password):
    valid = True

    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


password_input = input()
validate_password(password_input)
