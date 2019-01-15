import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def __reprt__(self):
        return "Creature {} of level  {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1,12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire): 
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll() 
        return base_roll / 2

class Wizard(Creature):
    def attack(self, creature):
        print("The Wizard {} attacks {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 15) * creature.level
        creature_roll = creature.get_defensive_roll()
        
        print("My Roll {}..".format(my_roll))
        print("{} rolls {}..".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("Wizard won")
            return True
        else:
            print("Creature Won")
            return False


