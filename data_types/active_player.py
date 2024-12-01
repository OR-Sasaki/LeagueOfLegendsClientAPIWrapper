from data_types.abilities import Abilities
from data_types.data_type_base import DataTypeBase
from data_types.full_runes import FullRunes
from data_types.champion_stats import ChampionStats


class ActivePlayer(DataTypeBase):
    abilities: Abilities
    champion_stats:ChampionStats
    current_gold:float
    full_runes:FullRunes
    level:int
    riot_id:str
    riot_id_game_name:str
    riot_id_tag_line:str
    summoner_name:str
    team_relative_colors:bool

    def parse(self, target_dict:dict):
        self.abilities = Abilities(target_dict['abilities'])
        self.champion_stats = ChampionStats(target_dict['championStats'])
        self.current_gold = target_dict['currentGold']
        self.full_runes = FullRunes(target_dict['fullRunes'])
        self.level = target_dict['level']
        self.riot_id = target_dict['riotId']
        self.riot_id_game_name = target_dict['riotIdGameName']
        self.riot_id_tag_line = target_dict['riotIdTagLine']
        self.summoner_name = target_dict['summonerName']
        self.team_relative_colors = target_dict['teamRelativeColors']
