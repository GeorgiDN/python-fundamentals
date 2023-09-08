n = int(input())

for i in range(n):
    curr_string = input()
    pure_string = True
    for j in curr_string:
        if j == ',' or j == '.' or j == '_':
            pure_string = False
            break
    if pure_string:
        print(f"{curr_string} is pure.")
    else:
        print(f"{curr_string} is not pure!")
      
