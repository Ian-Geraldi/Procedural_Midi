from models.pitch import Pitch
import os


def pitches_to_midtxt(pitches: list(Pitch), bpm: int = 80, file: str = "mao_esquerda.midtxt", howManyPerBar: int = 4):
    output_dir = "input"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, file)
    file_path = get_unique_filename(file_path)
    file = open(file_path, "w")
    file.write(str(bpm))
    file.write("\n")

    for i in range(len(pitches)):
        file.write(str(pitches[i]))
        bar_percentage = (i % howManyPerBar)/howManyPerBar
        if (bar_percentage < 1e-8 or abs(bar_percentage - 0.5) < 1e-8):
            file.write("f")
        else:
            file.write("p")
        file.write("1/" + str(howManyPerBar))
        file.write("\n")
    file.close()


def get_unique_filename(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{file_name}({counter}){file_extension}"
        counter += 1
    return file_path
