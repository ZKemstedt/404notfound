import random


class Character(object):
    def __init__(self, name, initiative, health, power, evasion, treasure=0):
        self.name = name
        self.initiative = initiative
        self.health = health
        self.power = power
        self.evasion = evasion
        self.treasure = treasure

    def special_power(self):
        raise NotImplementedError("Must be implemented!")

    def export(self) -> dict:
        character_class = self.__class__.__name__
        character_data = {}
        character_data[self.name] = {'class': character_class, 'health': self.health, 'treasure': self.treasure}
        return character_data


class Knight(Character):
    def __init__(self, name, treasure):
        super().__init__(name, 5, 9, 6, 4, treasure)

    def special_power(self):
        print("As a Knight you skip first attack from monster")


class Wizard(Character):
    def __init__(self, name, treasure):
        super().__init__(name, 6, 4, 9, 5, treasure)

    def special_power(self):
        escape_chance = random.randit(1, 100)
        if escape_chance <= 80:
            print("Escaped")
            return True
        else:
            return False


class Thief(Character):
    def __init__(self, name, treasure):
        super().__init__(name, 7, 5, 5, 7, treasure)

    def special_power(self):
        critical_hit = random.randit(1, 100)
        if critical_hit <= 25:
            print("Escaped")
            return True
        else:
            return False
