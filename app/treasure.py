class Treasure(object):

    def __init__(self, value, appearance_rate):
        self.value = value
        self.appearance_rate = appearance_rate


class Coins(treasure):

    def __init__(self):
        super().__init__(2, 0.4)


class Pouch(treasure):

    def __init__(self):
        super().__init__(6, 0.2)


class GoldJewelry(treasure):

    def __init__(self):
        super().__init__(10, 0.15)


class Gemstone(treasure):

    def __init__(self):
        super().__init__(14, 0.1)


class SmallTreasureChest(treasure):

    def __init__(self):
        super().__init__(20, 0.05)
