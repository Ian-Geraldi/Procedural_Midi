import numpy as np


graph = [
    [0, 0.34, 0.33, 0.33, 0, 0, 0],
    [0, 0, 0, 0, 0.7, 0, 0.3],
    [0, 0, 0, 0.3, 0, 0.7, 0],
    [0, 0, 0, 0, 0.7, 0.3, 0],
    [0.5, 0.1, 0.15, 0.1, 0, 0, 0.15],
    [0, 0.5, 0.5, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0, 0, 0],
]


def generate_progression(size):
    chordIndexes = []
    chordIndexes.append(1)
    for i in range(size):
        nodeProbabilities = graph[chordIndexes[len(chordIndexes)-1]-1]
        ansArray = np.random.choice(
            [0, 1, 2, 3, 4, 5, 6], 1, p=nodeProbabilities)
        chordIndexes.append(ansArray.tolist()[0]+1)
    return chordIndexes


# n = 30
# chordIndexes = []
# chordIndexes.append(0)

# for i in range(n):
#     nodeProbabilities = graph[chordIndexes[len(chordIndexes)-1]]
#     ansArray = np.random.choice([0, 1, 2, 3, 4, 5, 6], 1, p=nodeProbabilities)
#     chordIndexes.append(ansArray.tolist()[0])

# chordNames = []
# for value in chordIndexes:
#     for chordName, chordIndexes in names.items():
#         if chordIndexes == value:
#             chordNames.append(chordName)

# print(generate_progression(10))
