class Weapon:
    __bullets = 0

    def __init__(self, bullets: int):
        self.bullets = bullets
        Weapon.__bullets = self.bullets

    def shoot(self):
        if self.__bullets > 0:
            self.__bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.__bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)



# class Weapon:
#     def __init__(self, bullets: int):
#         self.bullets = bullets

#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return f"shooting..."
#         else:
#             return f"no bullets left"

#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"

# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
