from models.game_state import GameState

class Game:
    def __init__(self, state: GameState, players: list) -> None:
        self.state = state 
        self.players = players
    
    def json_serialize(self):
        json_data = dict()
        json_data['players'] = []
        json_data['state'] = GameState.Pending

        for player in self.players:
            player_json_data = player.json_serialize()
            json_data['players'].append(player_json_data)

        return json_data