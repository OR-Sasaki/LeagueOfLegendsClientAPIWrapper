from data_types.data_type_base import DataTypeBase

class Rune(DataTypeBase):
    id: str
    display_name: str
    raw_description: str
    raw_display_name: str

    def parse(self, target_dict:dict):
        self.id = target_dict['id']
        self.display_name = target_dict['displayName']
        self.raw_description = target_dict['rawDescription']
        self.raw_display_name = target_dict['rawDisplayName']
