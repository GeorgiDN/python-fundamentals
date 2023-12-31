password = input()

while True:
    command = input()
    if command == "Done":
        break

    parts = command.split()
    action = parts[0]

    if action == "TakeOdd":
        new_password = ""
        for idx, letter in enumerate(password):
            if idx % 2 != 0:
                new_password += letter
        password = new_password
        print(password)

    elif action == "Cut":
        cut_index, length = int(parts[1]), int(parts[2])
        password = password[:cut_index] + password[cut_index + length:]
        print(password)

    elif action == "Substitute":
        substring, substitute = parts[1], parts[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")





################################################   Task Description   ################################################
# Problem 1 - Password Reset
#
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.
#
# Yet again, you have forgotten your password. Naturally, it's not the first time this has happened.
# Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string, and afterward, until the command "Done" is given,
# you will be receiving strings with commands split by a single space. The commands will be the following:
#     • "TakeOdd"
#         o Takes only the characters at odd indices and concatenates them to obtain
#           the new raw password and then prints it.
#     • "Cut {index} {length}"
#         o Gets the substring with the given length starting from the given index from the password
#           and removes its first occurrence, then prints the password on the console.
#         o The given index and the length will always be valid.
#     • "Substitute {substring} {substitute}"
#         o If the raw password contains the given substring, replaces all of its occurrences
#           with the substitute text given and prints the result.
#         o If it doesn't, prints "Nothing to replace!".
# Input
#     • You will be receiving strings until the "Done" command is given.
# Output
#     • After the "Done" command is received, print:
#         o "Your password is: {password}"
# Constraints
#     • The indexes from the "Cut {index} {length}" command will always be valid.
