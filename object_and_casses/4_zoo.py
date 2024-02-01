class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        self._add_animal(species, name)
        self.__animals += 1

    def get_info(self, species):
        return self._show_info(species)

    # helper methods
    def _add_animal(self, curr_species, curr_name):
        if curr_species == "mammal":
            self.mammals.append(curr_name)
        elif curr_species == "fish":
            self.fishes.append(curr_name)
        elif curr_species == "bird":
            self.birds.append(curr_name)

    def _show_info(self, curr_species):
        result = ''
        if curr_species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif curr_species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif curr_species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {self.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())




# class Zoo:
#     __animals = 0
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []

#     def add_animals(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)

#         Zoo.__animals += 1

#     def get_info(self, species):
#         result = ""
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

#         result += f"Total animals: {Zoo.__animals}"
#         return result

# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())

# for i in range(count):
#     animal = input().split(" ")
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animals(species, name)

# info = input()
# print(zoo.get_info((info)))
