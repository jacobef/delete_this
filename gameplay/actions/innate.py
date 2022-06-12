from entities.entity import Entity
from gameplay.game import game
from gameplay.signal import Signal


def punch(puncher: Entity):
    game.send_signal(Signal(sender=puncher, damage=puncher.strength, damage_type="normal"),
                     should_send_to=lambda entity:
                         entity is not puncher
                         and abs(puncher.x_pos - entity.x_pos) < 100
                         and abs(puncher.y_pos - entity.x_pos) < 100
                     )
