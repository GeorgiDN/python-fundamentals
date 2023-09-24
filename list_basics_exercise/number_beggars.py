numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count  

for index in range(len(numbers)):
    number = int(numbers[index])
    beggars[index % beggars_count] += number  

print(beggars)
