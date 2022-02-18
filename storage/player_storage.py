
from player.abstract_player import AbstractPlayer, PlayerType
from player.player_factory import PlayerFactory
from storage.storage import Storage


class PlayerStorage(Storage):

    def get_by_username(self, username: str) -> AbstractPlayer:
        storage_data = self.storage.read()
        storage_player_data = storage_data['players']

        for player_data in storage_player_data:
            player_username = player_data['username']

            if player_username == username:
                player = PlayerStorage.__map_player_data_to_player(player_data)
                return player
        
        return None

    def get_players(self):
        storage_data = self.storage.read()
        storage_player_data = storage_data['players']

        # turn dict to players
        found_players = []

        for player_data in storage_player_data:
            player = PlayerStorage.__map_player_data_to_player(player_data)
            found_players.append(player)
        return found_players
    
    def update_players(self, data):
        storage_data = self.storage.read()
        storage_data['players'] = data
        self.storage.write_data(storage_data)  
    
    def update_player_hp_by_username(self, username: str, hp: int) -> bool:
        storage_data = self.storage.read()
        storage_player_data = storage_data['players']
        
        for i in range(len(storage_player_data)):
            player = storage_player_data[i]

            if player['username'] == username:
                storage_data['players'][i]['hp'] = hp
                self.storage.write_data(storage_data)
                return True
        
        return False
    
    @staticmethod
    def __map_player_data_to_player(data: dict) -> AbstractPlayer:
        player_type = PlayerType[data['type']]
        player_username = data['username']
        player_hp = data['hp']
        player = PlayerFactory.create_instance(player_type, player_username, player_hp)
        return player  