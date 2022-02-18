
# MVC - Model View Contoroller
from models.game import Game
from models.game_state import GameState
from player.abstract_player import AbstractPlayer
from storage.game_storage import GameStorage
import logging

from storage.player_storage import PlayerStorage

class GameUsecase:
    
    def __init__(self, game_storage: GameStorage, player_storage: PlayerStorage) -> None:
        self.game_storage = game_storage
        self.player_storage = player_storage

       
        self.state = self.game_storage.get_game_state()
        self.players = self.player_storage.get_players()
        #self.game = Game(state, players)

        self.init_state()
    
    def connect_player(self, player: AbstractPlayer) -> None:
       
        logging.info('connection started')
       
        if self.state != GameState.Pending:
            print('The game is already started. Please,try later')
            return

        found_player = self.player_storage.get_by_username(player.username)

        if found_player is not None:
            print('user with name {0} already exists'.format(player.username))
            return

        self.players.append(player)
        logging.debug('player appended to list')

        
        data = self.json_serialize()
        logging.debug('data serialized')

        self.player_storage.update_players(data['players'])
        logging.info('player connected')
    
    
    def disconnect_player(self, username: str):
        logging.info('disconnection started')
        for player in self.players:
            print(player.username)
            if player.username == username:
            
                self.players.remove(player)
                print('disconnected {0}'.format(username))
                
        logging.debug('player is removed')        
        data = self.json_serialize()
        logging.debug('data serialized')
        self.player_storage.update_players(data['players'])
        logging.info('player connected')

    def start(self):
        logging.info('starts updating game state to start')
        print('game start')
        self.game_storage.update_game_state(GameState.Start)
        logging.info('game state is updated')

    def end(self):
        logging.info('starts updating game state to end')
        print('game over')
        self.game_storage.update_game_state(GameState.Pending)
        logging.info('game state is updated')

    def init_state(self):
        logging.info('setting initial status')
        if self.state == None:
            
            self.game_storage.update_game_state(self.state.value)
            logging.info('initial status set')
        else:
            self.state = self.game_storage.get_game_state()
            logging.info('status is read from json')

    def json_serialize(self):
        json_data = dict()
        json_data['players'] = []
        json_data['state'] = GameState.Pending

        for player in self.players:
            player_json_data = player.json_serialize()
            json_data['players'].append(player_json_data)

        return json_data