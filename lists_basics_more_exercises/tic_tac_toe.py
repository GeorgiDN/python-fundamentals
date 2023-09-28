field = [list(map(int, input().split())) for _ in range(3)]

# Check rows
for row in field:
    if all(cell == 1 for cell in row):
        print("First player won")
        exit()
    if all(cell == 2 for cell in row):
        print("Second player won")
        exit()

# Check columns
for col in range(3):
    if all(row[col] == 1 for row in field):
        print("First player won")
        exit()
    if all(row[col] == 2 for row in field):
        print("Second player won")
        exit()

# Check diagonals
if all(field[i][i] == 1 for i in range(3)) or all(field[i][2 - i] == 1 for i in range(3)):
    print("First player won")
elif all(field[i][i] == 2 for i in range(3)) or all(field[i][2 - i] == 2 for i in range(3)):
    print("Second player won")
else:
    print("Draw!")
  
