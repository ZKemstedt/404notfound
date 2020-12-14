class Character(object):
    def __init__(self, name, initiative, health, power, evasion, treasure=0):
        self.name = name
        self.initiative = initiative
        self.health = health
        self.power = power
        self.evasion = evasion
        self.treasures = treasure

    def special_power(self):
        raise NotImplementedError("Must be implemented!")

    def export(self) -> dict:
        character_class = self.__class__.__name__
        character_data = {}
        character_data[self.name] = {'class': character_class, 'health': self.health, 'treasure': self.treasures}
        return character_data


class Knight(Character):
    def __init__(self, name, treasure=0):
        super().__init__(name, 5, 9, 6, 4, treasure)


class Wizard(Character):
    def __init__(self, name, treasure=0):
        super().__init__(name, 6, 4, 9, 5, treasure)


class Thief(Character):
    def __init__(self, name, treasure=0):
        super().__init__(name, 7, 5, 5, 7, treasure)
