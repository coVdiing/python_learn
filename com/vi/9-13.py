from random import randint

class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides =  randint(1,6)
        return self.sides

my_die = Die()
index = 1
while index <= 10:
    print my_die.roll_die()
    index+=1

