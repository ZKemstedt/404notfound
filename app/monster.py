class Monster(object):

    def __init__(self, health, evasion, power, initiative, name):
        self.health = health
        self.evasion = evasion
        self.power = power
        self.initiative = initiative
        self.name = name


class GiantSpider(Monster):

    def __init__(self):
        super().__init__(1, 3, 2, 7, 'GiantSpider')

    def __str__(self) -> str:
        return 'GiantSpider'

    def reset(self):
        self.health = 1


class Skeleton(Monster):

    def __init__(self):
        super().__init__(2, 3, 3, 4, 'Skeleton')

    def __str__(self) -> str:
        return 'Skeleton'

    def reset(self):
        self.health = 2


class Orc(Monster):

    def __init__(self):
        super().__init__(3, 4, 4, 6, 'Orc')

    def __str__(self) -> str:
        return 'Orc'

    def reset(self):
        self.health = 3


class Troll(Monster):

    def __init__(self):
        super().__init__(4, 2, 7, 2, 'Troll')

    def __str__(self) -> str:
        return 'Troll'

    def reset(self):
        self.health = 4
