def password_validator(password):
    invalid_messages = []
    if len(password) not in range(6, 11):
        invalid_messages.append("Password must be between 6 and 10 characters\n")
    if len([char for char in password if not char.isalnum()]) != 0:
        invalid_messages.append("Password must consist only of letters and digits\n")
    if len([char for char in password if char.isdigit()]) < 2:
        invalid_messages.append("Password must have at least 2 digits")

    if invalid_messages:
        return print("".join(invalid_messages))
    return print("Password is valid")


current_password = input()
password_validator(current_password)



# def validate_password(password):
#     valid = True

#     if not (6 <= len(password) <= 10):
#         print("Password must be between 6 and 10 characters")
#         valid = False

#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         valid = False

#     digit_count = sum(1 for char in password if char.isdigit())
#     if digit_count < 2:
#         print("Password must have at least 2 digits")
#         valid = False

#     if valid:
#         print("Password is valid")


# password_input = input()
# validate_password(password_input)
