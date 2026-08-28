#PSOmain.py ไว้ส่ง dataset เข้า Main_CI
import ML.SetUp.Main_CI as Main_CI
import numpy as np
import time

def acceptData(X , y):

    start_time = time.perf_counter()

    num_classes = len(np.unique(y))

    y_int = np.array(y, dtype=np.int32)
    best_mask, FitnessScore = Main_CI.run(X , y_int , num_classes)

    end_time = time.perf_counter()

    pso_execution_time = end_time - start_time

    selected = np.array(best_mask) == 1
    X_selected = X[:, selected]

    mask = []
    for index , i in enumerate(best_mask):
        if i == 1 :
            mask.append(index+1)

    return X_selected, mask , FitnessScore ,pso_execution_time
