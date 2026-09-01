# Benchmark/runner.py - Benchmark Execution & Orchestration Engine
import numpy as np
from sklearn.datasets import load_breast_cancer, load_wine, load_digits
from sklearn.preprocessing import StandardScaler

from ML.Computational_Intelligence.CI_Model.PSO.BPSO.PSOmain import acceptData as acceptData_cpp
from ML.Computational_Intelligence.CI_Model.PSO.Python_PSO.BPSO.PSOmain import acceptData as acceptData_python
from ML.model.prepare_data_universal import prepare_Data_universal

from .evaluator import evaluate_models
from .reporter import (
    print_header,
    print_dataset_info,
    print_trial_log,
    print_timing_summary,
    print_model_performance,
    print_overall_summary
)
from .visualizer import generate_all_plots


def benchmark_single_dataset(dataset_name="Breast Cancer", dataset_loader=load_breast_cancer, n_trials=5):
    """
    Runs benchmark trials on a single dataset for both C++ and Python PSO engines,
    and evaluates downstream ML models (Accuracy & Execution Time).
    """
    print_header(f"BENCHMARK: {dataset_name.upper()} ({n_trials} TRIALS)")

    data = dataset_loader()
    X, y = prepare_Data_universal(sklearn_dataset=data)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    num_samples, num_features = X.shape
    num_classes = len(np.unique(y))

    print_dataset_info(dataset_name, num_samples, num_features, num_classes, n_trials)

    # 1. Benchmark C++ PSO
    cpp_times = []
    cpp_scores = []
    cpp_selected_counts = []
    last_cpp_X_selected = None

    print("\n[1/2] Running C++ PSO engine...", flush=True)
    for trial in range(n_trials):
        X_selected, mask, score, exec_time = acceptData_cpp(X_scaled, y)
        exec_ms = exec_time * 1000.0
        cpp_times.append(exec_ms)
        cpp_scores.append(score)
        cpp_selected_counts.append(len(mask))
        last_cpp_X_selected = X_selected
        print_trial_log("C++ Engine", trial, exec_ms, score, len(mask), num_features)

    # 2. Benchmark Pure Python PSO
    py_times = []
    py_scores = []
    py_selected_counts = []
    last_py_X_selected = None

    print("\n[2/2] Running Pure Python PSO engine (Same exact formula)...", flush=True)
    for trial in range(n_trials):
        X_selected, mask, score, exec_time = acceptData_python(X_scaled, y)
        exec_ms = exec_time * 1000.0
        py_times.append(exec_ms)
        py_scores.append(score)
        py_selected_counts.append(len(mask))
        last_py_X_selected = X_selected
        print_trial_log("Python Engine", trial, exec_ms, score, len(mask), num_features)

    avg_cpp = float(np.mean(cpp_times))
    std_cpp = float(np.std(cpp_times))
    avg_py = float(np.mean(py_times))
    std_py = float(np.std(py_times))
    speedup = avg_py / avg_cpp if avg_cpp > 0 else 0

    print_timing_summary(
        dataset_name,
        avg_cpp, std_cpp, min(cpp_times), max(cpp_times),
        avg_py, std_py, min(py_times), max(py_times),
        speedup
    )

    # 3. Evaluate Downstream Classifier Performance (Accuracy + Execution Time)
    raw_models = evaluate_models(X, y)
    cpp_models = evaluate_models(last_cpp_X_selected, y)
    py_models = evaluate_models(last_py_X_selected, y)

    print_model_performance(raw_models, cpp_models, py_models)

    return {
        "dataset": dataset_name,
        "features": num_features,
        "samples": num_samples,
        "classes": num_classes,
        "cpp_times_ms": cpp_times,
        "py_times_ms": py_times,
        "cpp_avg_ms": avg_cpp,
        "cpp_std_ms": std_cpp,
        "py_avg_ms": avg_py,
        "py_std_ms": std_py,
        "speedup": speedup,
        "cpp_selected_avg": float(np.mean(cpp_selected_counts)),
        "py_selected_avg": float(np.mean(py_selected_counts)),
        "cpp_score_avg": float(np.mean(cpp_scores)),
        "py_score_avg": float(np.mean(py_scores)),
        "models": {
            "Raw": raw_models,
            "CPP": cpp_models,
            "Python": py_models
        }
    }


def run_all_benchmarks():
    """
    Main orchestration entry point:
    Runs all benchmark datasets, prints overall tables, and generates visualizations.
    """
    print_header("C++ vs PURE PYTHON PERFORMANCE BENCHMARK (PSO FEATURE SELECTION)")
    print("Methodology: Same objective function, same particle counts, same swarm", flush=True)
    print("             dynamics (w=0.7, c1=1.5, c2=1.5, sigmoid transfer), and", flush=True)
    print("             same early stopping patience (20 iterations).", flush=True)

    results = []
    # 1. Binary Classification (Breast Cancer - 30 features)
    results.append(benchmark_single_dataset("Breast Cancer (Binary)", load_breast_cancer, n_trials=5))

    # 2. Multiclass Classification (Wine - 13 features, 3 classes)
    results.append(benchmark_single_dataset("Wine (Multiclass)", load_wine, n_trials=5))

    # 3. Multiclass Higher Dimension (Digits - 64 features, 10 classes)
    results.append(benchmark_single_dataset("Digits (64 features, 10 classes)", load_digits, n_trials=3))

    # Print Summary Table
    print_overall_summary(results)

    # Generate All Visualizations
    generate_all_plots(results)
