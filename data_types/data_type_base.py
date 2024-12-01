from abc import abstractmethod


class DataTypeBase:
    data:dict

    def __init__(self, data:dict):
        self.data = data
        self.parse(data)

    @abstractmethod
    def parse(self, target_dict:dict):
        pass
