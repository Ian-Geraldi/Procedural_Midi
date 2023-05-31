import Harmonia.pattern_generator as pg
import numpy as np
from Modelos.pitch import Pitch
from Harmonia.RandomWalk import generate_progression

tom = np.random.randint(Pitch.A, Pitch.Ab)
pattern = pg.generate_pattern()
chords = generate_progression(len(pattern))


def _chord_notes(tom, grau):
    if type(tom) is not Pitch:
        raise Exception("tom must be a Pitch object")
    if grau == 7:
        return [tom, Pitch(tom+3), Pitch(tom+6)]
    elif grau == 5:
        return [tom, Pitch(tom+4), Pitch(tom+7), Pitch(tom+10)]
    elif grau == 1 or grau == 4:
        return [tom, Pitch(tom+4), Pitch(tom+7)]
    else:
        return [tom, Pitch(tom+3), Pitch(tom+7)]


def generate():
    pass


print("Pattern: " + str(pattern) + "\n")
print(_chord_notes(Pitch(tom), chords))
