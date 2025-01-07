class Character:
    name = "None"

    life = 100
    max_life = 100

    xp = 0
    max_xp = 100

    level = 1

    strength = 1
    resistance = 1
    initiative = 1
    dexterity = 1

    critical_multi = 1.1

    def __init__(self, name):
        self.name = name