from data_types.active_player import ActivePlayer
from data_types.data_type_base import DataTypeBase

class AllGameData(DataTypeBase):
    active_player:ActivePlayer

    def parse(self, target_dict:dict):
        self.active_player = ActivePlayer(target_dict['activePlayer'])
