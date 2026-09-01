# MainPSO.py - Python equivalent of MainPSO.cpp
# Prepares data matrix, sets particle count and iterations, runs EnginePSO

import numpy as np
from .Core.Engine import EnginePSO


def run_bpso(input_X, input_y, num_classes):
    """
    Exact 1:1 translation of C++ run_bpso in MainPSO.cpp
    Determines particle counts and iterations dynamically based on feature count.
    """
    if isinstance(input_X, np.ndarray):
        X = input_X.tolist()
    else:
        X = [list(row) for row in input_X]

    if isinstance(input_y, np.ndarray):
        y = input_y.astype(int).tolist()
    else:
        y = [int(v) for v in input_y]

    rows = len(X)
    cols = len(X[0])
    iterations = 10 * cols

    if cols < 20:
        amount_particles = 15
    elif cols <= 50:
        amount_particles = 25
    elif cols <= 100:
        amount_particles = 40
    elif cols <= 300:
        amount_particles = 60
    elif cols <= 600:
        amount_particles = 80
    elif cols <= 1000:
        amount_particles = 100
    else:
        amount_particles = 125

    engine = EnginePSO(amount_particles, iterations, X, y, num_classes)
    best_features, best_score = engine.run()

    return best_features, best_score
