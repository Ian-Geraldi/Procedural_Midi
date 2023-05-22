from Modelos import pitch
import numpy as np

tempos = [3, 4, 6, 8]


def generate_pattern():
    tempo = np.random.choice(tempos)
    notes = 7
    pattern = [0]
    for i in range(tempo-1):
        next_sign_odds = pattern[-1]/notes  # chance de ser sinal negativo
        next_sign = int(np.random.choice(
            [1, -1], size=1, p=[1-next_sign_odds, next_sign_odds]))
        delta = exponential() * next_sign
        next_note = np.clip(pattern[-1] + delta, 0, notes)
        pattern.append(next_note)

    return pattern


def exponential():
    lambda_param = 1
    continuous_values = np.random.exponential(scale=1/lambda_param, size=1)
    return 1 + int(np.round(continuous_values).astype(int))

    # Print the first 10 integer values
print(generate_pattern())
# print(generate_pattern())
