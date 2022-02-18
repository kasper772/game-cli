
# MVC - Model View Contoroller
from models.game_state import GameState
from storage.game_storage import GameStorage

class Game:
  
    def __init__(self, storage: GameStorage):
        self.storage = storage
        self.state = self.storage.get_game_state()
        self.players = self.storage.get_players()
    
    def connect_player(self, player):
        found_player = self.storage.get_by_username(player.username)

        if found_player is not None:
            print('user with name {0} already exists'.format(player.username))
            return

        self.players.append(player)
        print('connected {0}'.format(player.username))
        
        data = self.json_serialize()
        self.storage.update_players(data['players'])
    
        for player in self.players:
            print(player.username)
            if player.username == username:
            
                self.players.remove(player)
                print('disconnected {0}'.format(username))
              
                
        data = self.json_serialize()
        self.storage.update_players(data['players'])

    def start(self):
        print('game start')
        self.storage.update_game_state(GameState.Start)

    def end(self):
        print('game over')
        self.storage.update_game_state(GameState.Pending)

    def set_state(self):
        if self.storage.get_game_state() == None:
            
            self.storage.update_game_state(self.state.value)
        else:
            self.state = self.storage.get_game_state()

    def json_serialize(self):
        json_data = dict()
        json_data['players'] = []
        json_data['state'] = GameState.Pending


        for player in self.players:
            print(player)
            player_json_data = player.json_serialize()
            json_data['players'].append(player_json_data)

        return json_data