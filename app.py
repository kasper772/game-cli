import logging
from player.abstract_player import PlayerType
from models.game_state import GameState
from player.player_factory import PlayerFactory
from storage.game_storage import GameStorage
from storage.json_storage import JSONStorage, new_storage
from storage.player_storage import PlayerStorage
from usecase.game_usecase import GameUsecase
from usecase.player_usecase import PlayerUsecase


class App:
    def __init__(self, storage_path: str) -> None:
        json_storage = App.create_json_storage(storage_path)
        self.game_storage = GameStorage(json_storage)
        self.player_storage = PlayerStorage(json_storage)

    @staticmethod
    def create_json_storage(storage_path: str) -> JSONStorage:
        init_data = App.init_json_storage_data()
        storage = new_storage(storage_path, init_data)
        return storage

    @staticmethod
    def init_json_storage_data():
        json_data = dict()
        json_data["players"] = []
        return json_data

    def process(self, args) -> None:
        cmd = args.command

        try:
            if cmd == 'connect':
                self.connect(args)
            
            elif cmd == 'disconnect':
                self.disconnect(args)

            elif cmd == 'game':
                self.game(args)

            elif cmd == 'heal':
                self.heal(args)

            elif cmd == 'shoot':
                self.shoot(args)

        except Exception as err:
            logging.error('failed to run app with cli err: ' + err.__str__())


    def connect(self, args) -> None:
        player = PlayerFactory.create_instance(args.type, args.username)
        logging.debug('connecting player: {0} {1}'.format(player.username, player.type))
        

        GameUsecase(self.game_storage, self.player_storage).connect_player(player)
        logging.info('player was successfully connected: {0}'.format(player.username))
    
    def disconnect(self, args) -> None:
        GameUsecase(self.game_storage, self.player_storage).disconnect_player(args.username)
        logging.info('player was successfully disconnected: {0}'.format(args.username))
    
    def game(self, args) -> None:
        if args.state == GameState.Start:
            GameUsecase(self.game_storage, self.player_storage).start()
            return

        if args.state == GameState.End:
            GameUsecase(self.game_storage, self.player_storage).end()
    
    def heal(self, args):
        PlayerUsecase(self.game_storage, self.player_storage).heal(args.username)

    def shoot(self,args):
        PlayerUsecase(self.game_storage, self.player_storage).shoot(args.shooter, args.target)

        



