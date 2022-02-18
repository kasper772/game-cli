import logging
from usecase.game_usecase import GameUsecase
from models.game_state import GameState
from storage.game_storage import GameStorage
from storage.player_storage import PlayerStorage


class PlayerUsecase:
    def __init__(self, game_storage: GameStorage, player_storage: PlayerStorage) -> None:
        self.game_storage = game_storage
        self.player_storage = player_storage
    
    def shoot(self, shooter_username, target_username):
        if self.game_storage.get_game_state() == GameState.Start:
            shooter = self.player_storage.get_by_username(shooter_username)
            shooter_damage = shooter.get_damage()
            

            target = self.player_storage.get_by_username(target_username)
            

            target_updated_hp = target.hp - shooter_damage
            
            if target_updated_hp < 0: 
                target_updated_hp = 0
            
            if target_updated_hp == 0:
                GameUsecase(self.game_storage, self.player_storage).disconnect_player(target_username)
                logging.info("player {0} was killed".format(target_username))
            
                    
            
            self.player_storage.update_player_hp_by_username(target_username, target_updated_hp)
            logging.info("player {0} is shooting target {1} with damage {2}".format(
                shooter_username, target_username, shooter_damage))
                
            players = self.player_storage.get_players()
            if len(players) == 1:
                logging.info('player {0} is the winner!'.format(players[0].username))

        elif self.game_storage.get_game_state() == GameState.Pending:
            logging.info("the game hasn't started yet")

    def heal(self, username):
        if self.game_storage.get_game_state() == GameState.Start:
            player = self.player_storage.get_by_username(username)
            player.heal()

            self.player_storage.update_player_hp_by_username(username, player.hp)

        elif self.game_storage.get_game_state() == GameState.Pending:
            logging.info("the game hasn't started yet")