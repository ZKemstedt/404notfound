class Treasure(object):

    def __init__(self, value):
        self.value = value


class Coins(Treasure):

    def __init__(self):
        super().__init__(2)


class Pouch(Treasure):

    def __init__(self):
        super().__init__(6)


class GoldJewelry(Treasure):

    def __init__(self):
        super().__init__(10)


class Gemstone(Treasure):

    def __init__(self):
        super().__init__(14)


class SmallTreasureChest(Treasure):

    def __init__(self):
        super().__init__(20)
