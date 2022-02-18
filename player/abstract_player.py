from abc import ABC, abstractmethod


from models.player_type import PlayerType

class AbstractPlayer(ABC):
    def __init__(self, username: str, type: PlayerType, hp: int, damage: int) -> None:
        self.username = username    
        self.type = type
        self.hp = hp
        self.damage = damage
    
    def get_damage(self) -> int:
        return self.damage
        
    @abstractmethod
    def shoot(self, player):
        pass

    @abstractmethod
    def heal(self):
        pass

    def get_hp(self) -> int:
        return self.hp
    
    def set_hp(self, hp: int) -> None:
        self.hp = hp
    
    def json_serialize(self):
        json_data = dict()
        json_data['username'] = self.username
        json_data['type'] = self.type.value
        json_data['hp'] = self.hp
        json_data['damage'] = self.damage
        return json_data