from enum import Enum, auto

from entity import Entity
from action import MOVE_ACTION, INTERACT_ACTION, ABILITY_ACTION, ATTACK_ACTION, PASS_ACTION
class Being(Entity):
    def __init__(self, x_square: int, x_region: int, y_square: int, y_region: int, name: str):
        self.action_points = 10
        super().__init__(x_square, x_region, y_square, y_region, name)
