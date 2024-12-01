from data_types.data_type_base import DataTypeBase
from enum import Enum

class Ability(DataTypeBase):
    id:str
    ability_type:str
    ability_level:int
    display_name:str
    raw_description:str
    raw_display_name:str

    def parse(self, target_data:dict):
        self.ability_level = target_data.get('abilityLevel')
        self.display_name = target_data['displayName']
        self.raw_description = target_data['rawDescription']
        self.raw_display_name = target_data['rawDisplayName']

    def t(self, ability_type:str):
        self.ability_type = ability_type
        return self
