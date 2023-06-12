from enum import IntEnum


class Pitch(IntEnum):
    A = 1
    Bb = 2
    B = 3
    C = 4
    Db = 5
    D = 6
    Eb = 7
    E = 8
    F = 9
    Gb = 10
    G = 11
    Ab = 12
    A0 = 21
    Bb0 = 22
    B0 = 23
    C1 = 24
    Db1 = 25
    D1 = 26
    Eb1 = 27
    E1 = 28
    F1 = 29
    Gb1 = 30
    G1 = 31
    Ab1 = 32
    A1 = 33
    Bb1 = 34
    B1 = 35
    C2 = 36
    Db2 = 37
    D2 = 38
    Eb2 = 39
    E2 = 40
    F2 = 41
    Gb2 = 42
    G2 = 43
    Ab2 = 44
    A2 = 45
    Bb2 = 46
    B2 = 47
    C3 = 48
    Db3 = 49
    D3 = 50
    Eb3 = 51
    E3 = 52
    F3 = 53
    Gb3 = 54
    G3 = 55
    Ab3 = 56
    A3 = 57
    Bb3 = 58
    B3 = 59
    C4 = 60
    Db4 = 61
    D4 = 62
    Eb4 = 63
    E4 = 64
    F4 = 65
    Gb4 = 66
    G4 = 67
    Ab4 = 68
    A4 = 69
    Bb4 = 70
    B4 = 71
    C5 = 72
    Db5 = 73
    D5 = 74
    Eb5 = 75
    E5 = 76
    F5 = 77
    Gb5 = 78
    G5 = 79
    Ab5 = 80
    A5 = 81
    Bb5 = 82
    B5 = 83
    C6 = 84
    Db6 = 85
    D6 = 86
    Eb6 = 87
    E6 = 88
    F6 = 89
    Gb6 = 90
    G6 = 91
    Ab6 = 92
    A6 = 93
    Bb6 = 94
    B6 = 95
    C7 = 96
    Db7 = 97
    D7 = 98
    Eb7 = 99
    E7 = 100
    F7 = 101
    Gb7 = 102
    G7 = 103
    Ab7 = 104
    A7 = 105
    Bb7 = 106
    B7 = 107
    C8 = 108
    Db8 = 109
    D8 = 110
    Eb8 = 111
    E8 = 112
    F8 = 113
    Gb8 = 114
    G8 = 115
    Ab8 = 116
    A8 = 117
    Bb8 = 118
    B8 = 119
    C9 = 120
    Db9 = 121
    D9 = 122
    Eb9 = 123
    E9 = 124
    F9 = 125
    Gb9 = 126
    G9 = 127
    Ab9 = 128

    def __str__(self):
        return self.name

    def __add__(self, value):
        members = list(self.__class__)
        index = members.index(self)
        new_index = (index + value) % len(members)
        return members[new_index]

    def __sub__(self, value):
        members = list(self.__class__)
        index = members.index(self)
        new_index = (index - value) % len(members)
        return members[new_index]

    @classmethod
    def get_all(cls, *args, octave_range=None):
        notes_of_same_pitch = []
        for arg in args:
            if isinstance(arg, str):
                pitch = getattr(cls, arg)
            elif isinstance(arg, cls):
                pitch = arg
            else:
                raise TypeError("Argument must be of type str or Pitch")
            for note in cls:
                if (note.name == pitch.name or (note.name.startswith(pitch.name) and note.name[len(pitch.name)].isdigit())) and len(note.name) > 1 and note.name[-1].isdigit():
                    if octave_range is not None:
                        octave = int(note.name[-1])
                        if octave_range[0] <= octave <= octave_range[1]:
                            notes_of_same_pitch.append(note)
                    else:
                        notes_of_same_pitch.append(note)
        return sorted(notes_of_same_pitch, key=lambda note: note.value)

    @classmethod
    def get_notes(cls, *args, startNote=None, howManyNotes=None):
        pitches = list(args)

        # If startNote is not provided, select the first pitch as the startNote.
        if startNote is None:
            startNote = pitches[0]

        # If howManyNotes is not provided, return all the notes.
        if howManyNotes is None:
            howManyNotes = len(pitches)

        for i in range(len(pitches)):
            pitches[i] = pitches[i]+12
        for i, pitch in enumerate(pitches):
            while pitch < startNote:
                pitch = cls(pitch.value + 12)
            pitches[i] = pitch

        # Sort the pitches, select the first howManyNotes at or above startNote, and sort the selected pitches.
        pitches = sorted(pitch for pitch in pitches if pitch >= startNote)[
            :howManyNotes]

        return pitches

    # lembrar que o invert só aceita acordes dentro de um range de uma oitava. não pode ter duas oitavas da mesma nota.

    @classmethod
    def invert(cls, *args, bassCloseTo=None):
        pitches = list(args)
        distance = int(bassCloseTo) - int(pitches[0])
        while (True):
            newDistance = int(bassCloseTo) - int(pitches[0])
            if newDistance > distance:
                return pitches
            if abs(distance) < 2:
                return pitches
            if distance < 0:
                newBass = pitches[-1] - 12
                if newBass < 21:
                    return pitches
                pitches.insert(0, newBass)
                pitches.pop()
            else:
                newTopNote = pitches[0] + 12
                if newTopNote > 128:
                    return pitches
                pitches.append(newTopNote)
                pitches.pop(0)
        return pitches

    @classmethod
    def getAbsolute(cls, pitch):
        if pitch == 13:
            pitch = Pitch.A
        pitch = Pitch(pitch)
        name = ''.join(c for c in pitch.name if not c.isdigit())
        absolute_pitch = getattr(cls, name)
        return absolute_pitch


# print(Pitch.invert(Pitch.C3, Pitch.E3, Pitch.G3, bassCloseTo=Pitch.F3))
# print(Pitch.get_notes(Pitch.C, Pitch.E, Pitch.G,
#       startNote=Pitch.Db1, howManyNotes=4))
# print(Pitch.get_all('A', 'B', octave_range=[3, 5]))
# print(Pitch.get_all(Pitch.C, Pitch.D, octave_range=[1, 3]))
# print(Pitch.get_absolute(Pitch.Bb7))
