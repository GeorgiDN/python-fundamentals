# https://judge.softuni.org/Contests/Practice/Index/2031#0

def runout_of_products(quantity_food_, quantity_hay_, quantity_cover_):
    return quantity_food_ <= 0 or quantity_hay_ <= 0 or quantity_cover_ <= 0


def convert_kilograms_to_grams(*values):
    result = [value * 1000 for value in values]
    return map(float, result)


def convert_grams_to_kilograms(*values):
    result = [value / 1000 for value in values]
    return map(float, result)


def guinea_pig():
    out_of_products = False
    quantity_food = float(input())
    quantity_hay = float(input())
    quantity_cover = float(input())
    guinea_weight = float(input())

    quantity_food, quantity_hay, quantity_cover, guinea_weight = \
        convert_kilograms_to_grams(quantity_food, quantity_hay, quantity_cover, guinea_weight)

    for day in range(1, 31):
        quantity_food -= 300
        if runout_of_products(quantity_food, quantity_hay, quantity_cover):
            out_of_products = True
            print("Merry must go to the pet store!")
            break

        if day % 2 == 0:
            five_percent_of_food = (5 / 100) * quantity_food
            quantity_hay -= five_percent_of_food

        if day % 3 == 0:
            one_third_of_weight = guinea_weight / 3
            quantity_cover -= one_third_of_weight

    if not out_of_products:
        quantity_food, quantity_hay, quantity_cover, guinea_weight = \
            convert_grams_to_kilograms(quantity_food, quantity_hay, quantity_cover, guinea_weight)

        print(f"Everything is fine! Puppy is happy! "
              f"Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.")


guinea_pig()



#  #####################################################

# class Pig:
#     def __init__(self, food, hay, cover, pig_weight):
#         self.food = food
#         self.hay = hay
#         self.cover = cover
#         self.pig_weight = pig_weight
#         self.runout_of_products = False
# 
#     def take_care_for_pig(self):
#         for day in range(1, 30 + 1):
#             self.food = self._feed(self.food)
#             if not self.food:
#                 self.runout_of_products = True
#                 return self._go_to_store_message()
# 
#             if day % 2 == 0:
#                 self.hay = self._give_hay(self.hay, self.food)
#                 if not self.hay:
#                     self.run_out_of_products = True
#                     return self._go_to_store_message()
# 
#             if day % 3 == 0:
#                 self.cover = self._put_cover(self.cover, self.pig_weight)
#                 if not self.cover:
#                     self.run_out_of_products = True
#                     return self._go_to_store_message()
# 
#         self.food = self._convert_grams_to_kilograms(self.food)
#         self.hay = self._convert_grams_to_kilograms(self.hay)
#         self.cover = self._convert_grams_to_kilograms(self.cover)
#         happy_massage = self._puppy_if_happy_print(self.food, self.hay, self.cover)
#         return happy_massage
# 
# # Helper methods
#     def _feed(self, food_):
#         food_ -= 300
#         if food_ <= 0:
#             return False
#         return food_
# 
#     def _give_hay(self, hay_, food_):
#         five_percent_of_food = food_ * 0.05
#         hay_ -= five_percent_of_food
#         if hay_ <= 0:
#             return False
#         return hay_
# 
#     def _put_cover(self, cover_, weight):
#         one_third_of_pig_weight = weight / 3
#         cover_ -= one_third_of_pig_weight
#         if cover_ <= 0:
#             return False
#         return cover_
# 
#     def _go_to_store_message(self):
#         return "Merry must go to the pet store!"
# 
#     def _convert_grams_to_kilograms(self, value):
#         value /= 1000
#         return value
# 
#     def _puppy_if_happy_print(self, f, h, c):
#         return f"Everything is fine! Puppy is happy! Food: {f:.2f}, Hay: {h:.2f}, Cover: {c:.2f}."
# 
# 
# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# pig_weight = float(input()) * 1000
# 
# pig = Pig(food, hay, cover, pig_weight)
# print(pig.take_care_for_pig())



#  ######################### ##################################
# 
# def feed(food_):
#     food_ -= 300
#     if food_ <= 0:
#         return False
#     return food_
# 
# 
# def give_hay(hay_, food_):
#     five_percent_of_food = food_ * 0.05
#     hay_ -= five_percent_of_food
#     if hay_ <= 0:
#         return False
#     return hay_
# 
# 
# def put_cover(cover_, weight):
#     one_third_of_pig_weight = weight / 3
#     cover_ -= one_third_of_pig_weight
#     if cover_ <= 0:
#         return False
#     return cover_
# 
# 
# def go_to_store_message():
#     return "Merry must go to the pet store!"
# 
# 
# def puppy_if_happy_print(food_kg, hay_kg, cover_kg):
#     food_kg /= 1000
#     hay_kg /= 1000
#     cover_kg /= 1000
#     print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
# 
# 
# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# pig_weight = float(input()) * 1000
# run_out_of_products = False
# 
# 
# for day in range(1, 30 + 1):
#     food = feed(food)
#     if not food:
#         print(go_to_store_message())
#         run_out_of_products = True
#         break
# 
#     if day % 2 == 0:
#         hay = give_hay(hay, food)
#         if not hay:
#             print(go_to_store_message())
#             run_out_of_products = True
#             break
# 
#     if day % 3 == 0:
#         cover = put_cover(cover, pig_weight)
#         if not cover:
#             print(go_to_store_message())
#             run_out_of_products = True
#             break
# 
# if not run_out_of_products:
#     puppy_if_happy_print(food, hay, cover)





#  ######################### ##################################

# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# pig_wight = float(input()) * 1000
# runout_of_products = False
# 
# 
# for day in range(1, 30 + 1):
#     food -= 300
#     if food <= 0:
#         print("Merry must go to the pet store!")
#         runout_of_products = True
#         break
# 
#     if day % 2 == 0:
#         five_percent_of_food = food * 0.05
#         hay -= five_percent_of_food
#         if hay <= 0:
#             print("Merry must go to the pet store!")
#             runout_of_products = True
#             break
# 
#     if day % 3 == 0:
#         one_third_of_pig_weight = pig_wight / 3
#         cover -= one_third_of_pig_weight
#         if cover <= 0:
#             print("Merry must go to the pet store!")
#             runout_of_products = True
#             break
# 
# if not runout_of_products:
#     food_kg = food / 1000
#     hay_kg = hay / 1000
#     cover_kg = cover / 1000
#     print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
