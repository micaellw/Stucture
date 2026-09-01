# Benchmark/evaluator.py - Downstream Machine Learning Model Evaluator
# Measures both Accuracy and Execution/Inference Time for classifiers

import time
from ML.model.DecisionTree import DecisionModel
from ML.model.Random_Forest import RF
from ML.model.KNN import K_nn
from ML.model.SVM import svm
from ML.model.Train_Test_Split import Train_Test


def evaluate_models(X, y):
    """
    Evaluates Decision Tree, Random Forest, KNN, and SVM on given features X and labels y.
    Measures both Accuracy (%) and Execution Time (ms).
    """
    X_train, X_test, y_train, y_test = Train_Test(X, y)

    results = {}
    models = {
        "Decision Tree": DecisionModel,
        "Random Forest": RF,
        "KNN": K_nn,
        "SVM": svm
    }

    for name, model_func in models.items():
        start_time = time.perf_counter()
        accuracy = model_func(X_train, X_test, y_train, y_test)
        end_time = time.perf_counter()

        elapsed_ms = (end_time - start_time) * 1000.0

        results[name] = {
            "accuracy": accuracy * 100.0,
            "time_ms": elapsed_ms
        }

    return results
