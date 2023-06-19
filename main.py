# imports
from midtxt_generators import arpeggio
from parsers.pitches_to_midtxt import pitches_to_midtxt
from parsers.midtxt_to_midi import midtxt_to_midi
from scripts.move_to_old import move_to_old
import harmony.pattern_generator as pg
import numpy as np
from models.pitch import Pitch
from harmony.random_walk import generate_progression

# esse tempo é a duração da nota. 4 é uma semínima, 2 uma mínima, etc
tempo_arpeggio = 6

tom = Pitch(np.random.randint(Pitch.A, Pitch.Ab))
print("Vamos começar. Gerando o tom da música aleatoriamente. O tom é: ", Pitch(tom))

pattern1 = pg.generate_pattern(tempo_arpeggio)
print("Gerando o primeiro padrão de acordes. O padrão 1 é: " + str(pattern1))

pattern2 = pg.generate_pattern(tempo_arpeggio)
print("Gerando o primeiro padrão de acordes. O padrão 2 é: " + str(pattern2))

print("Gerando a progressão de acordes. A progressão é: ")
acordes = generate_progression(key=tom)

bpm = np.random.randint(40, 60)
print("Gerando o bpm aleatoriamente(um número entre 60 e 120). O bpm é: ", bpm)

arp1 = arpeggio.generate(acordes, pattern1, tom)
arp2 = arpeggio.generate(acordes, pattern2, tom)
arp = arp1 + arp2
print("Gerando o arpejo a partir da progressão de acordes")

pitches_to_midtxt(arp1, bpm=bpm, howManyPerBar=tempo_arpeggio)
pitches_to_midtxt(arp2, bpm=bpm, howManyPerBar=tempo_arpeggio)
print("Gerando o arquivo miditxt a partir dos arpejos gerados. Colocando ele na pasta \"input\"")

print("Gerando o midi a partir dos miditxts gerados. Ele se chama \"midiOutput.mid\" e está no diretório raiz do projeto")
midtxt_to_midi()

print("Movendo os arquivos miditxts gerados da pasta \"input\" para a pasta \"input_old\"")
move_to_old()
