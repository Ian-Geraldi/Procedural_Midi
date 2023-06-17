from models.pitch import Pitch
from models.velocity import Velocity
from fractions import Fraction


class Note:
    def __init__(self, ptch, velocity, Duration) -> None:
        self.pitch = Pitch[ptch]
        self.velocity = Velocity[velocity]
        self.duration = float(Fraction(Duration))
        pass
