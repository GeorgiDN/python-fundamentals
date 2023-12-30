food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000
run_out_of_products = False


def feed(food_):
    food_ -= 300
    if food_ <= 0:
        return False
    return food_


def give_hay(hay_, food_):
    five_percent_of_food = food_ * 0.05
    hay_ -= five_percent_of_food
    if hay_ <= 0:
        return False
    return hay_


def put_cover(cover_, weight):
    one_third_of_pig_weight = weight / 3
    cover_ -= one_third_of_pig_weight
    if cover_ <= 0:
        return False
    return cover_


def go_to_store_message():
    return "Merry must go to the pet store!"


def puppy_if_happy_print(food_kg, hay_kg, cover_kg):
    food_kg /= 1000
    hay_kg /= 1000
    cover_kg /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")


for day in range(1, 30 + 1):
    food = feed(food)
    if not food:
        print(go_to_store_message())
        run_out_of_products = True
        break

    if day % 2 == 0:
        hay = give_hay(hay, food)
        if not hay:
            print(go_to_store_message())
            run_out_of_products = True
            break

    if day % 3 == 0:
        cover = put_cover(cover, pig_weight)
        if not cover:
            print(go_to_store_message())
            run_out_of_products = True
            break

if not run_out_of_products:
    puppy_if_happy_print(food, hay, cover)
