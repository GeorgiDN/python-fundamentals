budged = int(input())
command = input()
total_price = 0

while command != 'End':
    product_price = int(command)
    budged -= product_price
    if budged < 0:
        print("You went in overdraft!")
        break
       
    command = input()
if command == 'End':
    print("You bought everything needed.")
  
