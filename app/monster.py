class Monster(object):

    def __init__(self, health, evasion, power, initiative, appearance_rate):
        self.health = health
        self.evasion = evasion
        self.power = power
        self.initiative = initiative
        self.appearance_rate = appearance_rate


class GiantSpider(Monster):

    def __init__(self):
        super().__init__(1, 3, 2, 7, 0.2)

    def __str__(self) -> str:
        return 'GiantSpider'


class Skeleton(Monster):

    def __init__(self):
        super().__init__(2, 3, 3, 4, 0.15)

    def __str__(self) -> str:
        return 'Skeleton'


class Orc(Monster):

    def __init__(self):
        super().__init__(3, 4, 4, 6, 0.1)

    def __str__(self) -> str:
        return 'Orc'


class Troll(Monster):

    def __init__(self):
        super().__init__(4, 2, 7, 2, 0.05)

    def __str__(self) -> str:
        return 'Troll'
