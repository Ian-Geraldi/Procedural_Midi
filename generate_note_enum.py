twelve_notes = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]

f = open("note.py", "a")
f.write("from enum import Enum\n\n")
f.write("class Note(Enum):\n")
octave = 0
for midi_note_index in range(21,129):
    note = twelve_notes[midi_note_index%12]
    if (note=="C"):
        octave+=1
    f.write("\t"+ note + str(octave) + " = ")
    f.write(str(midi_note_index)+"\n")


f.close()

#open and read the file after the appending:
f = open("note.py", "r")
print(f.read())