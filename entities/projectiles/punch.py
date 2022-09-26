from entities.projectile import Projectile
from gameplay.signal import Signal
class Punch(Projectile):
    def on_collide(self, target: "Entity"):
        # TODO fix this
        signal = Signal(sender = self, damage = self.source.strength, damage_type = "Normal")
        target.handle_signal(signal)
        print("Banana puree 🍌🍌🍌! Someone got punched.")

class Shoo(Projectile):
    def on_collide(self, target: "Entity"):
        signal = Signal(sender=self, damage=self.source.strength*0.5, damage_type="Normal")
        target.handle_signal(signal)
        print("Mango puree 🥭🥭🥭! Someone got shoo'd.")