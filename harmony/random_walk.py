import numpy as np
from models.pitch import Pitch
from models.chord import Chord, ChordType
import user_settings


def getDegree(chord: Chord, key: Pitch):
    if chord.pitch == key:
        return 1
    elif chord.pitch == Pitch.get_absolute(key+2):
        return 2
    elif chord.pitch == Pitch.get_absolute(key+4):
        return 3
    elif chord.pitch == Pitch.get_absolute(key+5):
        return 4
    elif chord.pitch == Pitch.get_absolute(key+7):
        return 5
    elif chord.pitch == Pitch.get_absolute(key+9):
        return 6
    elif chord.pitch == Pitch.get_absolute(key+11):
        return 7

    return 1
    raise Exception("Chord not diatonic to key")


def degreeToChord(grau, key):
    key = Pitch(key)
    if grau == 1:
        return Chord(Pitch(key), ChordType.Major)
    elif grau == 2:
        return Chord(Pitch(key+2), ChordType.Minor)
    elif grau == 3:
        return Chord(Pitch(key+4), ChordType.Minor)
    elif grau == 4:
        return Chord(Pitch(key+5), ChordType.Major)
    elif grau == 5:
        return Chord(Pitch(key+7), ChordType.Major)
    elif grau == 6:
        return Chord(Pitch(key+9), ChordType.Minor)
    elif grau == 7:
        return Chord(Pitch(key+11), ChordType.Diminished)
    raise Exception("Invalid chord degree")


def generate_progression(size=16, key: Pitch = Pitch.C):
    graph = user_settings.transitionMatrix
    chords = []
    chords.append(degreeToChord(1, key))
    lastDegree = 1
    for i in range(size):
        print(chords[-1])
        if user_settings.changeKeyOdds > np.random.rand():
            availableKeys = chords[-1].is_diatonic_to()
            availableKeys.remove(key)
            targetKey = Pitch.get_absolute(
                Pitch(np.random.choice(availableKeys)))
            key = targetKey
            lastDegree = getDegree(chords[-1], key)
            print("Key changed to", key, "degree = ", lastDegree)

        nodeProbabilities = graph[lastDegree-1]
        ansArray = np.random.choice(
            [0, 1, 2, 3, 4, 5, 6], 1, p=nodeProbabilities)
        lastDegree = ansArray.tolist()[0]+1
        chords.append(degreeToChord(lastDegree, key))
    return chords


# print(generate_progression(30))
