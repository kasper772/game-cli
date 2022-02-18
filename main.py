from app import App
from models.game_state import GameState
from player.abstract_player import PlayerType
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[
    logging.FileHandler("log/app.log"),
    logging.StreamHandler()
])

# abstract
# cli
# modules
# serialization/deserialization
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='cli game platform')
    command_parser = parser.add_subparsers(dest='command')

    # add cmd
    connect_command = command_parser.add_parser('connect')
    connect_command.add_argument('--username', type=str, help='username to connect player')
    connect_command.add_argument('--type', type=PlayerType, choices=list(PlayerType), help='username type for player connect')

    # remote player cmd
    disconnect_command = command_parser.add_parser('disconnect')
    disconnect_command.add_argument('--username', type=str, help='username to disconnect player')

    # start game cmd
    status_command = command_parser.add_parser('game')
    status_command.add_argument('--state', type=GameState, required=False, choices=list(GameState), help='enter game status')
    
    # shoot cmd
    shoot_command = command_parser.add_parser('shoot')
    shoot_command.add_argument('--shooter', type=str, help='username who is shooting')
    shoot_command.add_argument('--target', type=str,  help='the player who is being shot at')

    # heal cmd
    heal_command = command_parser.add_parser('heal')
    heal_command.add_argument('--username', type=str, help='username who is healing')
 
    # run app
    args = parser.parse_args()
    app = App('./game.json')
    app.process(args)