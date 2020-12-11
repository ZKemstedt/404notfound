class Monster(object):

    def __init__(self, health, evasion, power, initiative, appearance_rate, name):
        self.health = health
        self.evasion = evasion
        self.power = power
        self.initiative = initiative
        self.appearance_rate = appearance_rate
        self.name = name


class GiantSpider(Monster):

    def __init__(self):
        super().__init__(1, 3, 2, 7, 0.2, 'GiantSpider')


class Skeleton(Monster):

    def __init__(self):
        super().__init__(2, 3, 3, 4, 0.15, 'Skeleton')


class Orc(Monster):

    def __init__(self):
        super().__init__(3, 4, 4, 6, 0.1, 'Orc')


class Troll(Monster):

    def __init__(self):
        super().__init__(4, 2, 7, 2, 0.05, 'Troll')
