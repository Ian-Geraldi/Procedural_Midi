# imports
from midtxt_generators import arpeggio
from parsers.pitches_to_midtxt import pitches_to_midtxt
from parsers.midtxt_to_midi import midtxt_to_midi
from scripts.move_to_old import move_to_old
import harmony.pattern_generator as pg
import numpy as np
from models.pitch import Pitch
from harmony.random_walk import generate_progression
# generate the harmony
tom = np.random.randint(Pitch.A, Pitch.Ab)
print("Vamos começar. Gerando o tom da música aleatoriamente. O tom é: ", Pitch(tom))
pattern = pg.generate_pattern()
print("Gerando o padrão de acordes. O padrão é: " + str(pattern))
graus = generate_progression(len(pattern), key=tom)
print("Gerando a progressão de acordes a partir do padrão. A progressão é: " + str(graus))
bpm = np.random.randint(40, 60)
print("Gerando o bpm aleatoriamente(um número entre 60 e 120). O bpm é: ", bpm)
arp = arpeggio.generate(graus, pattern, tom)
print("Gerando o arpejo a partir da progressão de acordes" + str(arp))
print("Gerando o arquivo miditxt a partir dos arpejos gerados. Colocando ele na pasta \"input\"")
pitches_to_midtxt(arp, bpm=bpm, howManyPerBar=len(pattern))

print("Gerando o midi a partir dos miditxts gerados. Colocando ele na pasta \"output\"")
midtxt_to_midi()
move_to_old()
