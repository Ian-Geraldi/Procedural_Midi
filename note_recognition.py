from pitch import Pitch
from note import Note

def fromFileToNote(fileString):
    notes = []
    file = open(fileString)
    song = file.read()
    i = 0
    tempo = ""
    while(song[i].isnumeric()):
        tempo+=song[i]
        i+=1
    i+=1
    tempo = int(tempo)

    while(i<len(song)):
        ptch = ""
        velocity = ""
        duration = ""

        while(not (song[i]=='f' or song[i]=='m' or song[i]=='p')):
            ptch+=song[i]
            i+=1

        while(not song[i].isnumeric()):
            velocity+=song[i]
            i+=1

        while(song[i]!="\n"):
            duration+=song[i]
            i+=1

        i+=1

        print(ptch)
        print(velocity)
        print(duration)

        notes.append(Note(ptch,velocity,duration))
    return tempo, notes

