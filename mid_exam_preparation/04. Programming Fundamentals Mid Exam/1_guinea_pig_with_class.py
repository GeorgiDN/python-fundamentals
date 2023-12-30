class Pig:
    def __init__(self, food, hay, cover, pig_weight):
        self.food = food
        self.hay = hay
        self.cover = cover
        self.pig_weight = pig_weight
        self.runout_of_products = False

    def take_care_for_pig(self):
        for day in range(1, 30 + 1):
            self.food = self._feed(self.food)
            if not self.food:
                self.runout_of_products = True
                return self._go_to_store_message()

            if day % 2 == 0:
                self.hay = self._give_hay(self.hay, self.food)
                if not self.hay:
                    self.run_out_of_products = True
                    return self._go_to_store_message()

            if day % 3 == 0:
                self.cover = self._put_cover(self.cover, self.pig_weight)
                if not self.cover:
                    self.run_out_of_products = True
                    return self._go_to_store_message()

        self.food = self._convert_grams_to_kilograms(self.food)
        self.hay = self._convert_grams_to_kilograms(self.hay)
        self.cover = self._convert_grams_to_kilograms(self.cover)
        happy_massage = self._puppy_if_happy_print(self.food, self.hay, self.cover)
        return happy_massage

# Helper methods
    def _feed(self, food_):
        food_ -= 300
        if food_ <= 0:
            return False
        return food_

    def _give_hay(self, hay_, food_):
        five_percent_of_food = food_ * 0.05
        hay_ -= five_percent_of_food
        if hay_ <= 0:
            return False
        return hay_

    def _put_cover(self, cover_, weight):
        one_third_of_pig_weight = weight / 3
        cover_ -= one_third_of_pig_weight
        if cover_ <= 0:
            return False
        return cover_

    def _go_to_store_message(self):
        return "Merry must go to the pet store!"

    def _convert_grams_to_kilograms(self, value):
        value /= 1000
        return value

    def _puppy_if_happy_print(self, f, h, c):
        return f"Everything is fine! Puppy is happy! Food: {f:.2f}, Hay: {h:.2f}, Cover: {c:.2f}."


food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000

pig = Pig(food, hay, cover, pig_weight)
print(pig.take_care_for_pig())
