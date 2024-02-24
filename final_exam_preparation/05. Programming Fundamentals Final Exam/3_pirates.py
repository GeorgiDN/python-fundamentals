class Pirates:
    def __init__(self):
        self.target_cities = {}

    def start_pirate_task(self):
        already_sail = False
        while True:
            command = input()
            if command == "Sail":
                already_sail = True
                continue

            if command == "End":
                break

            if not already_sail:
                data = command.split("||")
                town, population, gold = data[0], int(data[1]), int(data[2])
                self.target_cities = self._add_town_to_target_cities(town, population, gold)

            else:
                info = command.split("=>")
                if info[0] == "Plunder":
                    town_plunder, people, gold_plunder = info[1], int(info[2]), int(info[3])
                    self.target_cities = self._plunder(town_plunder, people, gold_plunder)

                elif info[0] == "Prosper":
                    current_town, current_gold = info[1], int(info[2])
                    self.target_cities = self._prosper(current_town, current_gold)

        self._print_result()

    # Helper methods
    def _add_town_to_target_cities(self, town_, population_, gold_):
        if town_ not in self.target_cities:
            self.target_cities[town_] = [0, 0]
        self.target_cities[town_][0] += population_
        self.target_cities[town_][1] += gold_

        return self.target_cities

    def _plunder(self, town_, people_, gold_plunder_):
        self.target_cities[town_][0] -= people_
        self.target_cities[town_][1] -= gold_plunder_
        print(f"{town_} plundered! {gold_plunder_} gold stolen, {people_} citizens killed.")

        if self.target_cities[town_][0] <= 0 or self.target_cities[town_][1] <= 0:
            del self.target_cities[town_]
            print(f"{town_} has been wiped off the map!")

        return self.target_cities

    def _prosper(self, town_, gold_):
        if gold_ < 0:
            print("Gold added cannot be a negative number!")
        else:
            self.target_cities[town_][1] += gold_
            total_gold = self.target_cities[town_][1]
            print(f"{gold_} gold added to the city treasury. {town_} now has {total_gold} gold.")

        return self.target_cities

    def _print_result(self):
        if self.target_cities:
            print(f"Ahoy, Captain! There are {len(self.target_cities)} wealthy settlements to go to:")
            for city, towns_data in self.target_cities.items():
                num_of_people = towns_data[0]
                gold_left = towns_data[1]
                print(f"{city} -> Population: {num_of_people} citizens, Gold: {gold_left} kg")
        else:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")


pirates = Pirates()
pirates.start_pirate_task()






###################################################################################################################################################################
# class Pirates:
#     def __init__(self):
#         self.target_cities = {}
#
#     def start_pirate_task(self):
#         already_sail = False
#         while True:
#             command = input()
#             if command == "Sail":
#                 already_sail = True
#                 continue
#
#             if command == "End":
#                 break
#
#             if not already_sail:
#                 data = command.split("||")
#                 town, population, gold = data[0], int(data[1]), int(data[2])
#                 self.target_cities = self._add_town_to_target_cities(town, population, gold)
#
#             else:
#                 info = command.split("=>")
#                 if info[0] == "Plunder":
#                     town_plunder, people, gold_plunder = info[1], int(info[2]), int(info[3])
#                     self.target_cities = self._plunder(town_plunder, people, gold_plunder)
#
#                 elif info[0] == "Prosper":
#                     current_town, current_gold = info[1], int(info[2])
#                     self.target_cities = self._prosper(current_town, current_gold)
#
#     def __repr__(self):
#         repr_string = ""
#         if self.target_cities:
#             repr_string += f"Ahoy, Captain! There are {len(self.target_cities)} wealthy settlements to go to:\n"
#             for city, towns_data in self.target_cities.items():
#                 num_of_people = towns_data[0]
#                 gold_left = towns_data[1]
#                 repr_string += f"{city} -> Population: {num_of_people} citizens, Gold: {gold_left} kg\n"
#         else:
#             repr_string += "Ahoy, Captain! All targets have been plundered and destroyed!\n"
#         return repr_string
#
#     # Helper methods
#     def _add_town_to_target_cities(self, town_, population_, gold_):
#         if town_ not in self.target_cities:
#             self.target_cities[town_] = [0, 0]
#         self.target_cities[town_][0] += population_
#         self.target_cities[town_][1] += gold_
#
#         return self.target_cities
#
#     def _plunder(self, town_, people_, gold_plunder_):
#         self.target_cities[town_][0] -= people_
#         self.target_cities[town_][1] -= gold_plunder_
#         print(f"{town_} plundered! {gold_plunder_} gold stolen, {people_} citizens killed.")
#
#         if self.target_cities[town_][0] <= 0 or self.target_cities[town_][1] <= 0:
#             del self.target_cities[town_]
#             print(f"{town_} has been wiped off the map!")
#
#         return self.target_cities
#
#     def _prosper(self, town_, gold_):
#         if gold_ < 0:
#             print("Gold added cannot be a negative number!")
#         else:
#             self.target_cities[town_][1] += gold_
#             total_gold = self.target_cities[town_][1]
#             print(f"{gold_} gold added to the city treasury. {town_} now has {total_gold} gold.")
#
#         return self.target_cities
#
#
# pirates = Pirates()
# pirates.start_pirate_task()
# print(repr(pirates))
