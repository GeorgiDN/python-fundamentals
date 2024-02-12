def is_price_positive_number(tax_):
    return tax_ >= 0


def increase_taxes_with_twenty_percent(prices_without_taxes_, prices_with_taxes_):
    prices_with_taxes_ = [price * 1.20 for price in prices_without_taxes_]
    return prices_with_taxes_


def take_ten_percent_of_discount(total_sum_, prices_with_taxes_):
    total_sum_ = total_sum_ * 0.9
    return total_sum_


def take_taxes(taxes_, prices_without_taxes_, prices_with_taxes_):
    taxes_ = sum(prices_with_taxes_) - sum(prices_without_taxes_)
    return taxes_



def print_result(total_price_without_taxes_, taxes_, total_sum_):
    return print("Congratulations you've just bought a new computer!\n"
                 f"Price without taxes: {total_price_without_taxes_:.2f}$\n"
                 f"Taxes: {taxes_:.2f}$\n"
                 "-----------\n"
                 f"Total price: {total_sum_:.2f}$")


def computer_store():
    prices_without_taxes = []
    prices_with_taxes = []
    taxes = 0
    type_of_customer = ""

    while True:
        command = input()
        if command == "special":
            type_of_customer = "special"
            break
        elif command == "regular":
            type_of_customer = "regular"
            break
        current_tax = float(command)

        if not is_price_positive_number(current_tax):
            print("Invalid price!")
            continue

        prices_without_taxes.append(current_tax)

    if prices_without_taxes:
        total_price_without_taxes = sum(prices_without_taxes)
        prices_with_taxes = increase_taxes_with_twenty_percent(prices_without_taxes, prices_with_taxes)
        taxes = take_taxes(taxes, prices_without_taxes, prices_with_taxes)
        total_sum = sum(prices_with_taxes)
        if type_of_customer == "special":
            total_sum = take_ten_percent_of_discount(total_sum, prices_with_taxes)

        print_result(total_price_without_taxes, taxes, total_sum)

    else:
        print("Invalid order!")


computer_store()






# price_without_task = 0
# while True
#     command = input()

#     if command == 'special' or command == 'regular'
#         break

#     price = float(command)
#     if price  0
#         print('Invalid price!')
#         continue

#     price_without_task += price

# taxes = price_without_task  0.2
# final_price = price_without_task + taxes

# if command == 'special'
#     if price_without_task  0
#         discount = final_price  0.1
#         final_price = final_price - discount
#         print(fCongratulations you've just bought a new computer!n
#               fPrice without taxes {price_without_task.2f}$n
#               fTaxes {taxes.2f}$n
#               f-----------n
#               fTotal price {final_price.2f}$)
#     else
#         print('Invalid order!')

# elif command == 'regular'
#     if price_without_task  0
#         print(fCongratulations you've just bought a new computer!n
#               fPrice without taxes {price_without_task.2f}$n
#               fTaxes {taxes.2f}$n
#               f-----------n
#               fTotal price {final_price.2f}$)
#     else
#         print('Invalid order!')




######################################################################################  CONDITION  ##########################################################################################################################################
#httpsjudge.softuni.orgContestsPracticeIndex2517#0

# Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive. 
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print Invalid price! on the console and continue with the next price.
# If the total price is equal to zero, you should print Invalid order! on the console.
# Input
# •	You will receive numbers representing prices (without tax) until the command special or regular
# Output
# •	The receipt should be in the following format 
# Congratulations you've just bought a new computer!
# Price without taxes {total price without taxes}$
# Taxes {total amount of taxes}$
# -----------
# Total price {total price with taxes}$
# Note All prices should be displayed to the second digit after the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!
