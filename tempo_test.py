from mido import Message, MidiFile, MidiTrack
from pitch import Pitch
from tempo import Tempo
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

tempo = Tempo(60)

track.append(Message('program_change', program=12, time=0))
for i in range(4):
    track.append(Message('note_on', note=Pitch.C4, velocity=64, time=0))
    track.append(Message('note_off', note=Pitch.C4, velocity=127, time=tempo.Time(1)))
for i in range(8):
    track.append(Message('note_on', note=Pitch.C4, velocity=64, time=0))
    track.append(Message('note_off', note=Pitch.C4, velocity=127, time=tempo.Time(1/2)))
for i in range(16):
    track.append(Message('note_on', note=Pitch.C4, velocity=64, time=0))
    track.append(Message('note_off', note=Pitch.C4, velocity=127, time=tempo.Time(1/4)))

mid.save('tempo_test.mid')