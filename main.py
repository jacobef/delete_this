import sys
from enum import Enum, auto

from entities.entity import Entity
from entities.projectile import Projectile, PickupS, coffee
from gameplay.action import nothing_action
from gameplay.game import *
from entities.npc import NPC
from entities.player import Player

import pygame
import time

from graphics.sprite import EntitySprite, ProjectileSprite
from graphics.init import init_graphics
from graphics.tick import tick_graphics
from physics.vector2d import Vector2D

TPS = 60
"""Ticks per second. All tick() methods should be called at this rate."""
from time import sleep

class ProgramActionType(Enum):
    """Represents a type of action that the player can take on the game itself, e.g. quitting."""
    QUIT = auto()


def quit_game():
    """Exits the program."""
    pygame.quit()
    time.sleep(0.5)
    sys.exit(0)

def run_game():
    """The main function. Starts the program."""
    init_graphics()
    player: Player = Player(position=Vector2D(50, 400),
                            current_action=nothing_action,
                            max_health=500, max_mana=500, max_energy=500,
                            speed=5, strength=100,
                            base_energy_regen=100, base_mana_regen=10, base_health_regen=5,
                            )
    npc: NPC = NPC("enn pee cee", position=Vector2D(500, 500),
                   max_health=1000, max_mana=200, max_energy=500, base_energy_regen=2, base_mana_regen=1,
                   sprite=EntitySprite(img_path="goblin.jpeg", scale=[50, 50]), speed=0.5)
    joe = Entity("joe", position=Vector2D(100, 100),
    sprite=EntitySprite(img_path="Banana.jpeg", scale=[100,100]))
    strength = PickupS("Hulk feel strong", strength=100, duration=1000000, position=Vector2D(560, 90), source=joe, sprite=ProjectileSprite(img_path="important.jpeg", scale=[25, 25]), initial_velocity=Vector2D(0,0))
    coffie = coffee("Hulk feel stronger", strength=1000, duration=10000, position=Vector2D(250, 30), source=joe,
                      sprite=ProjectileSprite(img_path="VERY_IMPORTANT.jpeg", scale=[25, 25]),
                      initial_velocity=Vector2D(0, 0))
    game.set_player(player)
    game.spawn_entity(player)
    game.spawn_entity(npc)
    game.spawn_entity(joe)
    game.spawn_entity(strength)
    game.spawn_entity(coffie)
    game.ping_everything()
    """
    ns = strength * 1000000
    ns = ns - strength
    """
    while True:
        time.sleep(1 / TPS)
        tick_graphics()
        game.tick()


run_game()
