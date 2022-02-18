from player.base_player import BasePlayer
from player.skeleton_player import SkeletonPlayer
from player.abstract_player import PlayerType


class PlayerFactory:
    @staticmethod
    def create_instance(player_type, username, hp=100):
        if player_type == PlayerType.Base:
            return BasePlayer(username, hp)
        elif player_type == PlayerType.Skeleton:
            return SkeletonPlayer(username, hp)
        else:
            raise ValueError('can`t create unexpected player type {0} for {1}'.format(type(player_type), username))
