food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_wight = float(input()) * 1000
runout_of_products = False


for day in range(1, 30 + 1):
    food -= 300
    if food <= 0:
        print("Merry must go to the pet store!")
        runout_of_products = True
        break

    if day % 2 == 0:
        five_percent_of_food = food * 0.05
        hay -= five_percent_of_food
        if hay <= 0:
            print("Merry must go to the pet store!")
            runout_of_products = True
            break

    if day % 3 == 0:
        one_third_of_pig_weight = pig_wight / 3
        cover -= one_third_of_pig_weight
        if cover <= 0:
            print("Merry must go to the pet store!")
            runout_of_products = True
            break

if not runout_of_products:
    food_kg = food / 1000
    hay_kg = hay / 1000
    cover_kg = cover / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
  
