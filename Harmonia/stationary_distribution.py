import numpy as np
from scipy.linalg import eig
from UserSettings import UserSettings

# Transition matrix
p = UserSettings.transitionMatrix

# Solve eigenvalue problem
values, vectors = eig(P.T)

# Find vector where eigenvalue is 1
idx = np.where(np.abs(values - 1) < 1e-8)[0][0]

# Normalise the corresponding eigenvector to get the stationary distribution
stationary = np.real(vectors[:, idx])
stationary /= np.sum(stationary)

print(stationary)
