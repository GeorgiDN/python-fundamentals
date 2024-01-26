class DoubleChar:

    def __init__(self):
        pass

    def implement_double_char(self):
        command = self._take_input()

        while command != 'End':
            if command != 'SoftUni':
                for i in command:
                    print(i * 2, end='')
                print()

            command = self._take_input()

    def _take_input(self):
        return input()


double_char = DoubleChar()
double_char.implement_double_char()


# command = input()

# while command != 'End':
#     if command == 'SoftUni':
#         command = input()

#     for i in command:
#         print(i * 2, end='')
#     print()
#     command = input()
