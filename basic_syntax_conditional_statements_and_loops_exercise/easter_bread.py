budget = float(input())
price_1kg_flour = float(input())

price_1_pack_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25

price_250ml_milk = price_1l_milk / 4

colored_eggs = 0

number_of_loaves = 0

one_bread_price = price_1_pack_eggs + price_1kg_flour + price_250ml_milk

while one_bread_price < budget:
    budget -= one_bread_price
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
