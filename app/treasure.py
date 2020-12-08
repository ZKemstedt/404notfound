class Treasure(object):

    def __init__(self, value, appearance_rate):
        self.value = value
        self.appearance_rate = appearance_rate


class Coins(Treasure):

    def __init__(self):
        super().__init__(2, 0.4)


class Pouch(Treasure):

    def __init__(self):
        super().__init__(6, 0.2)


class GoldJewelry(Treasure):

    def __init__(self):
        super().__init__(10, 0.15)


class Gemstone(Treasure):

    def __init__(self):
        super().__init__(14, 0.1)


class SmallTreasureChest(Treasure):

    def __init__(self):
        super().__init__(20, 0.05)
