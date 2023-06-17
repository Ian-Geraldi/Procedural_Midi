from models.pitch import Pitch


def major(key: Pitch):
    return [key, key+2, key+4, key+5, key+7, key+9, key+11]
