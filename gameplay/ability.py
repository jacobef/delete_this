from typing import Callable, Any

from entities.projectile import Projectile
from entities.projectiles.punch import Punch, Shoo
from gameplay.action import GameAction
from gameplay.game import game
from gameplay.signal import Signal
from graphics.sprite import ProjectileSprite
from physics.vector2d import Vector2D
from input import input
from pygame import MOUSEBUTTONUP
from pygame import mouse
from math import atan2


class Ability:
    """An info class used to generate an action (e.g. punch) and apply the cost of it to the player."""

    def __init__(self, name: str, resolve_time: int,
                 function_to_call: Callable[["Entity"], Any], can_move: bool = False,
                 energy_cost: int = 0, mana_cost: int = 0, health_cost: int = 0
                 ):
        self.name = name

        self.resolve_time = resolve_time
        self.function_to_call = function_to_call

        self.can_move = can_move
        self.energy_cost = energy_cost
        self.mana_cost = mana_cost
        self.health_cost = health_cost

    def as_action(self, player: "Player"):
        """Generates and returns the action."""
        return GameAction(self.name, self.resolve_time, self.can_move, lambda: None,
                          lambda: self.function_to_call(player))


def player_punch_resolve(puncher: "Entity"):
    """The function to be called when a punch action resolves."""
    mouse_pos = Vector2D.from_tuple(mouse.get_pos())
    initial_pos = Vector2D(puncher.position.x+puncher.sprite.scale[0]/2, puncher.position.y+puncher.sprite.scale[1]/2)
    projectile_to_mouse = Vector2D(mouse_pos.x-initial_pos.x, mouse_pos.y-initial_pos.y)
    angle = atan2(projectile_to_mouse.y, projectile_to_mouse.x)
    hand_projectile = Punch(name="punch (rename this)", duration=150, source=puncher,
                            position=initial_pos,
                            sprite=ProjectileSprite("captain_alex.png", scale=[20, 20]),
                            initial_velocity=Vector2D.from_polar(10, angle))
    game.spawn_entity(hand_projectile)

def npc_punch_resolve(puncher: "Entity"):
    """The function to be called when a punch action resolves."""
    player_pos = game.player.position
    initial_pos = Vector2D(puncher.position.x+puncher.sprite.scale[0]/2, puncher.position.y+puncher.sprite.scale[1]/2)
    projectile_to_player = Vector2D(player_pos.x-initial_pos.x, player_pos.y-initial_pos.y)
    angle = atan2(projectile_to_player.y, projectile_to_player.x)
    hand_projectile = Punch(name="punch (rename this)", duration=150, source=puncher,
                            position=initial_pos,
                            sprite=ProjectileSprite("punch_for_open_world.png", scale=[20, 20]),
                            initial_velocity=Vector2D.from_polar(10, angle))
    game.spawn_entity(hand_projectile)

def shoo_resolve(puncher: "Entity"):
    mouse_pos = Vector2D.from_tuple(mouse.get_pos())
    initial_pos = Vector2D(puncher.position.x + puncher.sprite.scale[0] / 2,
                           puncher.position.y + puncher.sprite.scale[1] / 2)
    projectile_to_mouse = Vector2D(mouse_pos.x - initial_pos.x, mouse_pos.y - initial_pos.y)
    angle = atan2(projectile_to_mouse.y, projectile_to_mouse.x)
    hand_projectile = Shoo(name="punch (rename this)", duration=300, source=puncher,
                            position=initial_pos,
                            sprite=ProjectileSprite("hahaha.png", scale=[20, 20]),
                            initial_velocity=Vector2D.from_polar(20, angle))
    game.spawn_entity(hand_projectile)


empty_slot = Ability("empty slot", 0, lambda player: None)

player_punch = Ability("punch", 250, player_punch_resolve,
                       energy_cost=50, mana_cost=10)
npc_punch = Ability("punch", 250, npc_punch_resolve, energy_cost=50, mana_cost=10)

shoo = Ability("shoo", 250, shoo_resolve, energy_cost=50, mana_cost=10)
