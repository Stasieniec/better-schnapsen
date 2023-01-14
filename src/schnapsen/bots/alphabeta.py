"""Alpha–beta pruning is basically an optimized version of minimax."""
from typing import Optional

from schnapsen.game import Bot, Move, PlayerPerspective


class AlphaBetaBot(Bot):
    __max_depth = -1
    __randomize = True

    def __init__(self, randomize: bool = True, depth: int = 8) -> None:
        self.__randomize = randomize
        self.__max_depth = depth

    def get_move(self, player_perspective: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        raise NotImplementedError()
