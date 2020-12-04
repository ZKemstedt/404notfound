class monsters(object):

    def __init__(self, health, evasion, power, initiative, commonality):
        self.health = health
        self.evasion = evasion
        self.power = power
        self.initiative = initiative
        self.commonality = commonality

class GiantSpider(monsters):

    def __init__(self):
        super().__init__(1, 3, 2, 7, 20%)

class Skeleton(monsters):

    def __init__(self):
        super().__init__(2, 3, 3, 4, 15%)

class Orc(monsters):

    def __init__(self):
        super().__init__(3, 4, 4, 6, 10%)
    
class Troll(monsters):

    def __init__(self):
        super().__init__(4, 2, 7, 2, 5%)
