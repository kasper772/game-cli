
from models.game_state import GameState
from storage.storage import Storage


class GameStorage(Storage):

    def get_game_state(self) -> GameState:
        data = self.storage.read()
        raw_state = data["state"]
        state = GameState[raw_state]
        return state
    
    def update_game_state(self, state: GameState):
        storage_data = self.storage.read()
        storage_data['state'] = state.value
        self.storage.write_data(storage_data)
        