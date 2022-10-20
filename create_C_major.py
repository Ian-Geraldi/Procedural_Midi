from mido import Message, MidiFile, MidiTrack
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


#está funcionando, mas tá soando harpejado


track.append(Message('program_change', program=12, time=0))

#c4
track.append(Message('note_on', note=64, velocity=64, time=0))
track.append(Message('note_off', note=64, velocity=127, time=32))

#e4
track.append(Message('note_on', note=60, velocity=64, time=0))
track.append(Message('note_off', note=60, velocity=127, time=32))

#g4
track.append(Message('note_on', note=67, velocity=64, time=0))
track.append(Message('note_off', note=67, velocity=127, time=32))

mid.save('c_major.mid')