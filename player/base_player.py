from player.abstract_player import PlayerType
from player.abstract_player import AbstractPlayer


class BasePlayer(AbstractPlayer):
    def __init__(self, username, hp):
        super().__init__(username, PlayerType.Base, hp, 20)
    
    def shoot(self, player):
        print('player {0} is shooting {1}'.format(player, self.username))

        player_hp = self.get_hp()
        self.set_hp(player_hp - self.damage)
    
    def heal(self):
        heal_hp = 20

        print('player {0} is healing by {1}'.format(self.username, heal_hp))

        hp = self.get_hp()
        self.set_hp(hp + heal_hp)
