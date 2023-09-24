factor = int(input())
count = int(input())

calculated_result = []

num = factor
while len(calculated_result) < count:
    calculated_result.append(num)
    num += factor

print(calculated_result)
