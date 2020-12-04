class Monster(object):

    def __init__(self, health, evasion, power, initiative, appearance_rate):
        self.health = health
        self.evasion = evasion
        self.power = power
        self.initiative = initiative
        self.appearance_rate = appearance_rate

class GiantSpider(monster):

    def __init__(self):
        super().__init__(1, 3, 2, 7, 0.2)

class Skeleton(monster):

    def __init__(self):
        super().__init__(2, 3, 3, 4, 0.15)

class Orc(monster):

    def __init__(self):
        super().__init__(3, 4, 4, 6, 0.1)
    
class Troll(monster):

    def __init__(self):
        super().__init__(4, 2, 7, 2, 0.05)
