from mido import Message, MidiFile, MidiTrack
from Modelos.pitch import Pitch
from Modelos.tempo import Tempo
from Modelos.velocity import Velocity
from Parsers.note_recognition import fromFileToNote
import os


mid = MidiFile(type=1)
directory = "Input"

for midtxtfile in os.listdir(directory):

    file = os.path.join(directory, midtxtfile)
    track = MidiTrack()
    mid.tracks.append(track)

    bpm, notes = fromFileToNote(file)
    tempo = Tempo(bpm)

    track.append(Message('program_change', program=12, time=0))

    i = 0
    notes[i]

    # primeira nota
    track.append(
        Message('note_on', note=notes[i].pitch, velocity=notes[i].velocity, time=0))
    track.append(
        Message('note_off', note=notes[i].pitch, velocity=notes[i].velocity, time=0))
    i += 1

    # todas as outras
    for i in range(1, len(notes)):

        track.append(Message(
            'note_on', note=notes[i].pitch, velocity=notes[i].velocity, time=tempo.Time(notes[i-1].duration)))
        # observe que olhamos para a duração da última nota pra sabermos quando tocar a próxima, daí o notes[i-1].duration
        track.append(
            Message('note_off', note=notes[i].pitch, velocity=notes[i].velocity, time=0))


track.append(Message('note_on', note=Pitch.C4, velocity=0, time=tempo.Time(2)))
track.append(Message('note_off', note=Pitch.C4, velocity=0, time=0))

mid.save('yourMidi.mid')
