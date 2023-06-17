import numpy as np
from scipy.linalg import eig
from userSettings import user_settings

p = user_settings.transitionMatrix

values, vectors = eig(p.T)

idx = np.where(np.abs(values - 1) < 1e-8)[0][0]

stationary = np.real(vectors[:, idx])
stationary /= np.sum(stationary)

print(stationary)
