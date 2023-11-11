import re

total_price = 0
furniture_list = []

while True:
    text = input()
    if text == 'Purchase':
        break

    # pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)\b"
    # With this pattern above we have to change match.group with name,not number!
    pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)\b"
    matches = re.finditer(pattern, text)

    for match in matches:
        furniture_name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(4))

        total_price += price * quantity
        furniture_list.append(furniture_name)

print("Bought furniture:")
for furniture in furniture_list:
    print(f"{furniture}")
print(f"Total money spend: {total_price:.2f}")
