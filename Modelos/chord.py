from Modelos.pitch import Pitch
from enum import IntEnum


class ChordType(IntEnum):
    Major = 0
    Minor = 1
    Diminished = 2
    Augmented = 3
    Major7M = 4
    Minor7 = 5
    Dominant7 = 6
    Diminished7 = 7

    def __str__(self):
        return self.name


class Chord:
    def __init__(self, pitch: Pitch, type: ChordType):
        self.pitch = Pitch.getAbsolute(pitch)
        self.type = type

    def __str__(self):
        return str(self.pitch) + " " + str(self.type)

    __repr__ = __str__

    def notes(self) -> list(Pitch):
        type = self.type
        pitch = self.pitch
        if type == ChordType.Major:
            ret = [pitch, Pitch(pitch+4), Pitch(pitch+7)]
        elif type == ChordType.Minor:
            ret = [pitch, Pitch(pitch+3), Pitch(pitch+7)]
        elif type == ChordType.Diminished:
            ret = [pitch, Pitch(pitch+3), Pitch(pitch+6), Pitch(pitch+9)]
        elif type == ChordType.Augmented:
            ret = [pitch, Pitch(pitch+4), Pitch(pitch+8)]
        elif type == ChordType.Major7M:
            ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+11)]
        elif type == ChordType.Minor7:
            ret = [pitch, Pitch(pitch+3), Pitch(pitch+7), Pitch(pitch+10)]
        elif type == ChordType.Dominant7:
            ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+10)]
        elif type == ChordType.Diminished7:
            ret = [pitch, Pitch(pitch+3), Pitch(pitch+6), Pitch(pitch+10)]
        for i in range(len(ret)):
            ret[i] = Pitch.getAbsolute(ret[i])
        return ret

    def availableTensions(self) -> list(Pitch):
        type = self.type
        pitch = self.pitch
        if type == ChordType.Major:
            ret = [Pitch(pitch+2), Pitch(pitch+9), Pitch(pitch+11)]
        elif type == ChordType.Minor:
            ret = [Pitch(pitch+2), Pitch(pitch+5), Pitch(pitch+10)]
        elif type == ChordType.Diminished:
            ret = [Pitch(pitch+2), Pitch(pitch+4), Pitch(pitch+7)]
        for i in range(len(ret)):
            ret[i] = Pitch.getAbsolute(ret[i])
        return ret

    def isDiatonicTo(self):
        type = self.type
        pitch = self.pitch
        if type == ChordType.Major:
            ret = [pitch, pitch+5, pitch+7]

        if type == ChordType.Minor:
            ret = [pitch+3, pitch+8, pitch+10]

        if type == ChordType.Diminished:
            ret = [pitch, pitch+3, pitch+6, pitch+9]

        if ret is None:
            raise Exception("Invalid chord type")

        for i in range(len(ret)):
            ret[i] = Pitch.getAbsolute(ret[i])
        return ret


# def chordNotes(pitch: Pitch, type: ChordType, grau: int = 0) -> list(Pitch):
#         if type == ChordType.Major or grau == 1 or grau == 4 or grau == 5:
#             ret = [pitch, Pitch(pitch+4), Pitch(pitch+7)]
#         elif type == ChordType.Minor or grau == 2 or grau == 3 or grau == 6:
#             ret = [pitch, Pitch(pitch+3), Pitch(pitch+7)]
#         elif type == ChordType.Diminished or grau == 7:
#             ret = [pitch, Pitch(pitch+3), Pitch(pitch+6)]
#         elif type == ChordType.Augmented:
#             ret = [pitch, Pitch(pitch+4), Pitch(pitch+8)]
#         elif type == ChordType.Major7M:
#             ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+11)]
#         elif type == ChordType.Minor7:
#             ret = [pitch, Pitch(pitch+3), Pitch(pitch+7), Pitch(pitch+10)]
#         elif type == ChordType.Dominant7:
#             ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+10)]
#         elif type == ChordType.Diminished7:
#             ret = [pitch, Pitch(pitch+3), Pitch(pitch+6), Pitch(pitch+10)]
#         else:
#             raise Exception("Invalid chord type")
#         for i in range(len(ret)):
#             ret[i] = Pitch.get_absolute(ret[i])
#         return ret


# chord = Chord(Pitch.C, ChordType.Minor)
# print(chord.notes())
# print(chord.availableTensions())
# print(chord.isDiatonicTo())
