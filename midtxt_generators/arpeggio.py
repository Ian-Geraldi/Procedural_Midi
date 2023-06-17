import harmony.pattern_generator as pg
import numpy as np
from typing import List
from models.pitch import Pitch
from models.chord import Chord, chordNotes
from harmony.random_walk import generate_progression
from parsers.pitches_to_midtxt import pitches_to_midtxt


def generate(chords: List[Chord], pattern, tom):
    notes = []
    lastBass = tom+44
    for chord in chords:
        chord_notes = chordNotes(chord.pitch, type=chord.type)
        possibilities = Pitch.get_all(*chord_notes, octave_range=[2, 4])
        inverted = Pitch.invert(*possibilities, bassCloseTo=lastBass)
        lastBass = inverted[0]
        for i in pattern:
            notes.append(possibilities[i])
    return notes


# pitches_to_midtxt(generate(graus, bpm, pattern, tom),
#                   howManyPerBar=len(pattern))
