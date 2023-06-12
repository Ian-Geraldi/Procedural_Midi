import Harmonia.pattern_generator as pg
import numpy as np
from Modelos.pitch import Pitch
from Modelos.chord import chordNotes
from Harmonia.RandomWalk import generateProgression
from Parsers.pitches_to_midtxt import pitches_to_midtxt

tom = np.random.randint(Pitch.A, Pitch.Ab)
pattern = pg.generate_pattern()
graus = generateProgression(len(pattern))
bpm = 80


def generate(graus, bpm, pattern, tom):
    notes = []
    lastBass = tom+44
    for grau in graus:
        chord_notes = chordNotes(Pitch(tom), grau=grau)
        possibilities = Pitch.get_all(*chord_notes, octave_range=[2, 4])
        inverted = Pitch.invert(*possibilities, bassCloseTo=lastBass)
        lastBass = inverted[0]
        for i in pattern:
            notes.append(possibilities[i])
    return notes


pitches_to_midtxt(generate(graus, bpm, pattern, tom),
                  howManyPerBar=len(pattern))
