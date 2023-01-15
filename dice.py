import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return random.randint(1, self.sides)


print("Roll 6 times a die with 6 sides")
die = Die()
for i in range(6):
    print(die.roll_die())

print("Roll 10 times a die with 10 sides")
die_10 = Die()
die_10.sides = 10
for i in range(10):
    print(die_10.roll_die())

print("Roll 10 times a die with 20 sides")
die_20 = Die()
die_20.sides = 20
for i in range(10):
    print(die_20.roll_die())
