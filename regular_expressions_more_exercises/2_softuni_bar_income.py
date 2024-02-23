import re


def extract_name_and_calculate_cost(data_):
    name_pattern = r"%([A-Z][a-z]+)\%"
    product_pattern = r"<([\w]+)>"
    count_pattern = r"\|(\d+)\|"
    price_pattern = r"(\d+(\.\d+)*)\$"
    name = re.findall(name_pattern, data_)[0]
    product = re.findall(product_pattern, data_)[0]
    count = int(re.findall(count_pattern, data_)[0])
    price = float(re.findall(price_pattern, data_)[0][0])
    cost = count * price
    print(f"{name}: {product} - {cost:.2f}")
    return cost


def soft_uni_bar_income():
    total_income = 0
    while True:
        data = input()
        if data == "end of shift":
            break
        pattern = r"(%[A-Z]{1}[a-z]+\%)([^\|\$\%\.])*(<[\w]+>)([^\|\$\%\.])*(\|\d+\|)([^\|\$\%\.])*(\d+(\.\d+)*\$)"
        matches = re.findall(pattern, data)
        if matches:
            cost = extract_name_and_calculate_cost(data)
            total_income += cost

    print(f"Total income: {total_income:.2f}")


soft_uni_bar_income()




# import re


# def softuni_bar_income():
#     total_income = 0
#     pattern = r"%(?P<customer>[A-Z][a-z]+)%[^\|\$\%\.]*(?P<product><\w+)>[^\|\$\%\.]*\|(?P<count>\d+)\|[A-Za-z\s]*(?P<price>\d+(\.\d+)*)\$"

#     while True:
#         found_matches = False
#         data = input()
#         if data == "end of shift":
#             break

#         matches = re.finditer(pattern, data)

#         for match in matches:
#             customer = match.group("customer")
#             product = match.group("product")[1:]
#             count = int(match.group("count"))
#             price = float(match.group("price"))
#             total_price = count * price
#             found_matches = True

#         if found_matches:
#             total_income += total_price
#             print(f"{customer}: {product} - {total_price:.2f}")

#     print(f"Total income: {total_income:.2f}")


# softuni_bar_income()


