class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.price > money:
            return "Sorry, not enough money"
        if self.owner:
            return "Car already sold"

        self.owner = owner
        change = abs(self.price - money)
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)





# class Vehicle:
#     def __init__(self, type, model, price):
#         self.type = type
#         self.model = model
#         self.price = price
#         self.owner = None

#     def buy(self, money: int, owner: str):
#         if self.price <= money and self.owner == None:
#             self.owner = owner
#             return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"
#         elif self.price > money:
#             return f"Sorry, not enough money"
#         elif self.owner != None:
#             return f"Car already sold"

#     def sell(self):
#         if self.owner != None:
#             self.owner = None
#         else:
#             return f"Vehicle has no owner"

#     def __repr__(self):
#         if self.owner != None:
#             return f"{self.model} {self.type} is owned by: {self.owner}"
#         else:
#             return f"{self.model} {self.type} is on sale: {self.price}"


# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)

