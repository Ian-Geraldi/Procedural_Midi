import Harmonia.pattern_generator as pg
import numpy as np
from Modelos.pitch import Pitch
from Harmonia.RandomWalk import generate_progression

tom = np.random.randint(Pitch.A, Pitch.Ab)
pattern = pg.generate_pattern()
graus = generate_progression(len(pattern))
bpm = 80


def _chord_notes(tom, grau):
    if type(tom) is not Pitch:
        raise Exception("tom must be a Pitch object")
    if grau == 7:
        ret = [tom, Pitch(tom+3), Pitch(tom+6)]
    elif grau == 5:
        ret = [tom, Pitch(tom+4), Pitch(tom+7), Pitch(tom+10)]
    elif grau == 1 or grau == 4:
        ret = [tom, Pitch(tom+4), Pitch(tom+7)]
    else:
        ret = [tom, Pitch(tom+3), Pitch(tom+7)]
    for i in range(len(ret)):
        ret[i] = Pitch.get_absolute(ret[i])
    return ret


def generate(graus, bpm, pattern, tom):
    notes = []
    note_length = 1/(len(pattern))
    lastBass = tom+44
    for grau in graus:
        notes = _chord_notes(Pitch(tom), grau)
        possibilities = Pitch.get_all(*notes, octave_range=[2, 2])
        inverted = Pitch.invert(*possibilities, bassCloseTo=lastBass)
        lastBass = inverted[0]
        for i in pattern:
            notes.append(possibilities[i])


print(generate(graus, bpm, pattern, tom))
