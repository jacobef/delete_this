from math import atan2

from entities.being import Being
from entities.projectiles.punch import Punch
from gameplay.ability import npc_punch
from gameplay.game import game
from graphics.sprite import ProjectileSprite
from physics.vector2d import Vector2D


class NPC(Being):
    """Will add more to this later"""

    def tick(self):
        npc_to_player = game.player.position - self.position
        angle = atan2(npc_to_player.y, npc_to_player.x)
        self.velocity=Vector2D.from_polar(2.5, angle)
        self.attempt_ability(npc_punch)
        super().tick()



