from Modelos.pitch import Pitch


def chord(pitch: Pitch, type: str = "", grau: int = 0) -> list(Pitch):
    if type == "major" or grau == 1 or grau == 4 or grau == 5:
        ret = [pitch, Pitch(pitch+4), Pitch(pitch+7)]
    elif type == "minor" or grau == 2 or grau == 3 or grau == 6:
        ret = [pitch, Pitch(pitch+3), Pitch(pitch+7)]
    elif type == "diminished" or grau == 7:
        ret = [pitch, Pitch(pitch+3), Pitch(pitch+6)]
    elif type == "augmented":
        ret = [pitch, Pitch(pitch+4), Pitch(pitch+8)]
    elif type == "major7M":
        ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+11)]
    elif type == "minor7":
        ret = [pitch, Pitch(pitch+3), Pitch(pitch+7), Pitch(pitch+10)]
    elif type == "dominant7":
        ret = [pitch, Pitch(pitch+4), Pitch(pitch+7), Pitch(pitch+10)]
    elif type == "diminished7":
        ret = [pitch, Pitch(pitch+3), Pitch(pitch+6), Pitch(pitch+10)]
    else:
        raise Exception("Invalid chord type")
    for i in range(len(ret)):
        ret[i] = Pitch.get_absolute(ret[i])
    return ret


def tensions(pitch: Pitch, type: str) -> list(Pitch):
    if type == "major":
        ret = [Pitch(pitch+2), Pitch(pitch+9), Pitch(pitch+11)]
    elif type == "minor":
        ret = [Pitch(pitch+2), Pitch(pitch+5), Pitch(pitch+10)]
    elif type == "diminished":
        ret = [Pitch(pitch+2), Pitch(pitch+4), Pitch(pitch+7)]
