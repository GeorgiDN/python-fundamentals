class Party:
    def __init__(self):
        self.people = []

    def add_people(self):
        while True:
            name = input()
            if name == "End":
                break

            self.people.append(name)


party = Party()
party.add_people()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")





# class Party:
#     def __init__(self):
#         self.people = []

# party = Party()

# line = input()
# while line != 'End':
#     party.people.append(line)
#     line = input()

# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")




# Second way

# class Party:
#     def __init__(self):
#         self.people = []

#     def add_person(self, name):
#         self.people.append(name)

#     def get_party_info(self):
#         party_info = {
#             'going': ', '.join(self.people),
#             'total': len(self.people)
#         }

#         result = f"Going: {party_info['going']}\nTotal: {party_info['total']}"

#         return result

# party = Party()

# while True:
#     name = input()

#     if name == 'End':
#         break
#     party.add_person(name)

# print(party.get_party_info())
