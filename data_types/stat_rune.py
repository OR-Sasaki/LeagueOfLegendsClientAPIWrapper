from data_types.data_type_base import DataTypeBase

class StatRune(DataTypeBase):
    id: str
    raw_description: str

    def parse(self, target_dict:dict):
        self.id = target_dict['id']
        self.raw_description = target_dict['rawDescription']
