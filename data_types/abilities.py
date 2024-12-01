from data_types.ability import Ability
from data_types.data_type_base import DataTypeBase

def to_ability(target_dict:dict, t:str):
    return Ability(target_dict[t]).t(t)

class Abilities(DataTypeBase):
    abilities: [Ability]

    def parse(self, target_dict:dict):
        types = ['Passive', 'Q', 'W', 'E', 'R']
        self.abilities = {types[i]: to_ability(target_dict, types[i]) for i in range(0, len(types), 1)}

