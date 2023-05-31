from mido import Message, MidiFile, MidiTrack
from app.Modelos.pitch import Pitch
from app.Modelos.tempo import Tempo
from app.Modelos.velocity import Velocity
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

tempo = Tempo(120)

track.append(Message('program_change', program=12, time=0))


track.append(Message('note_on', note=Pitch.C4,
             velocity=Velocity.ffff, time=tempo.Time(10)))

track.append(Message('note_on', note=Pitch.E4,
             velocity=Velocity.ff, time=tempo.Time(1)))

track.append(Message('note_on', note=Pitch.G4,
             velocity=Velocity.mf, time=tempo.Time(1)))

track.append(Message('note_off', note=Pitch.C4, velocity=127, time=0))
track.append(Message('note_off', note=Pitch.E4, velocity=127, time=0))
track.append(Message('note_off', note=Pitch.G4, velocity=127, time=0))

track.append(Message('note_on', note=Pitch.E4,
             velocity=Velocity.p, time=tempo.Time(1)))


track.append(Message('note_on', note=Pitch.C4,
             velocity=Velocity.ppp, time=tempo.Time(1)))


mid.save('c_major.mid')
