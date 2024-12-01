from data_types.data_type_base import DataTypeBase
from data_types.rune import Rune
from data_types.stat_rune import StatRune

class FullRunes(DataTypeBase):
    general_runes:[Rune]
    keystone:Rune
    primary_rune_tree:Rune
    secondary_rune_tree:Rune
    stat_runes:[StatRune]

    def parse(self, target_dict:dict):
        self.general_runes = [Rune(d) for d in target_dict['generalRunes']]
        self.keystone = Rune(target_dict['keystone'])
        self.primary_rune_tree = Rune(target_dict['primaryRuneTree'])
        self.secondary_rune_tree = Rune(target_dict['secondaryRuneTree'])
        self.stat_runes = [StatRune(d) for d in target_dict['statRunes']]
