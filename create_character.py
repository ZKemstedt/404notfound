import random


def choose_character_type():
    error = ('You can only enter 1, 2 or 3')
    while True:
        try:
            choice = int(input(
                'Choose character type.\n'
                '(1) Knight, (2) Wizard or (3) Thief.\n'
                ))
        except TypeError:
            print(error)
            continue
        except ValueError:
            print(error)
            continue

        if choice < 0 or choice > 3:
            print(error)
            continue
        break

    return choice


class Character(object):
    def __init__(self, name, initiative, health, power, evasion):
        self.name = name
        self.initiative = initiative
        self.health = health
        self.power = power
        self.evasion = evasion

    def special_power(self):
        raise NotImplementedError("Must be implemented!")


class Knight(Character):
    def __init__(self, name):
        super().__init__(name, 5, 9, 6, 4)

    def special_power(self):
        print("As a Knight you skip first attack from monster")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 6, 4, 9, 5)

    def special_power(self):
        escape_chance = random.randit(1, 100)
        if escape_chance <= 80:
            print("Escaped")
            return True
        else:
            return False


class Thief(Character):
    def __init__(self, name):
        super().__init__(name, 7, 5, 5, 7)

    def special_power(self):
        critical_hit = random.randit(1, 100)
        if critical_hit <= 25:
            print("Escaped")
            return True
        else:
            return False
