# # Character class example

# class Character(object):

#     def __init__(self, name, health, evasion, power, initiative):
#         self.name = name
#         self.health = health
#         self.evasion = evasion
#         self.power = power
#         self.initiative = initiative

#     def special_power(self):
#         raise NotImplementedError('Must be implemented!')
    
#     def attack(self):
#         pass

#     def flee(self):
#         pass


# class Wizard(Character):

#     def __init__(self, name):
#         super().__init__(name, 4, 5, 9, 6)
    
#     def special_power(self):
#         print("ljusken lol")
    
#     def flee(self):
#         self.special_power()


# class Knight(Character):

#     def __init__(self, name):
#         super().__init__(name, 9, 4, 6, 5)
    
#     def special_power(self):
#         print('block')



#
#
#
#
#
# yaml

import yaml
from pathlib import Path


filename = 'text.yml'
p = Path(filename)


data = {
    "spelare": {
        "anton": {
            'health': 5,
            'skatter': 9999
            # osv
        },
        'ludvig': {
            'health': 5,
            'skatter': 0
        }
    },
    "statistik": 5
}


with p.open(mode='w', encoding="UTF-8") as f:
    yaml.dump(data, f)

with p.open(mode='r', encoding="UTF-8") as f:
    data = yaml.load(f)

