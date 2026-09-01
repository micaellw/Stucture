# PSOmain.py - Python equivalent of PSO/BPSO/PSOmain.py
# Accepts dataset, benchmarks execution time, and extracts selected features

import time
import numpy as np
from ..MainPSO import run_bpso


def acceptData(X, y):
    """
    Python equivalent of acceptData in C++ PSOmain.py
    Measures execution time, extracts best features mask, and slices X.
    """
    start_time = time.perf_counter()

    num_classes = len(np.unique(y))
    y_int = np.array(y, dtype=np.int32)

    best_mask, fitness_score = run_bpso(X, y_int, num_classes)

    end_time = time.perf_counter()
    pso_execution_time = end_time - start_time

    selected = np.array(best_mask) == 1
    X_selected = X[:, selected]

    mask = []
    for index, i in enumerate(best_mask):
        if i == 1:
            mask.append(index + 1)

    return X_selected, mask, fitness_score, pso_execution_time


acceptData_python = acceptData
