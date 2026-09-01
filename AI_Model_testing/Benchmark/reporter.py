# Benchmark/reporter.py - Console Reporting and Table Formatting

def print_header(title):
    print(f"\n{'='*75}", flush=True)
    print(f" {title}", flush=True)
    print(f"{'='*75}", flush=True)


def print_dataset_info(name, samples, features, classes, trials):
    print(f"Dataset Name   : {name}", flush=True)
    print(f"Dataset Shape  : {samples} samples x {features} features", flush=True)
    print(f"Classes Count  : {classes} classes", flush=True)
    print(f"Trials Count   : {trials} runs per engine", flush=True)
    print(f"{'-'*75}", flush=True)


def print_trial_log(engine_name, trial_idx, time_ms, score, selected_count, total_features):
    print(f"  [{engine_name}] Trial {trial_idx+1:02d}: Time = {time_ms:8.3f} ms | Score = {score:8.4f} | Selected = {selected_count:2d}/{total_features}", flush=True)


def print_timing_summary(dataset_name, avg_cpp, std_cpp, min_cpp, max_cpp, avg_py, std_py, min_py, max_py, speedup):
    print(f"\n{'-'*75}", flush=True)
    print(f" TIMING SUMMARY ({dataset_name})", flush=True)
    print(f"{'-'*75}", flush=True)
    print(f"  C++ Engine Avg Time   : {avg_cpp:8.3f} ms (+/- {std_cpp:6.3f} ms)", flush=True)
    print(f"  C++ Engine Min / Max  : {min_cpp:8.3f} ms / {max_cpp:8.3f} ms", flush=True)
    print(f"  Python Engine Avg Time: {avg_py:8.3f} ms (+/- {std_py:6.3f} ms)", flush=True)
    print(f"  Python Engine Min/Max : {min_py:8.3f} ms / {max_py:8.3f} ms", flush=True)
    print(f"  -------------------------------------------------------------------------", flush=True)
    print(f"  >>> SPEEDUP RESULT    : C++ is {speedup:.2f}x FASTER than Pure Python <<<", flush=True)
    print(f"  -------------------------------------------------------------------------", flush=True)


def print_model_performance(raw_models, cpp_models, py_models):
    print(f"\n{'-'*75}", flush=True)
    print(f" DOWNSTREAM CLASSIFIER: ACCURACY & EXECUTION TIME COMPARISON", flush=True)
    print(f"{'-'*75}", flush=True)
    print(f"{'Model':<14} | {'Without PSO (Full)':<20} | {'C++ PSO Features':<20} | {'Python PSO Features':<20}", flush=True)
    print(f"{'':<14} | {'Acc (%)':<8} {'Time (ms)':<10} | {'Acc (%)':<8} {'Time (ms)':<10} | {'Acc (%)':<8} {'Time (ms)':<10}", flush=True)
    print(f"{'-'*75}", flush=True)

    for model_name in raw_models.keys():
        r_acc, r_t = raw_models[model_name]["accuracy"], raw_models[model_name]["time_ms"]
        c_acc, c_t = cpp_models[model_name]["accuracy"], cpp_models[model_name]["time_ms"]
        p_acc, p_t = py_models[model_name]["accuracy"], py_models[model_name]["time_ms"]

        print(f"{model_name:<14} | {r_acc:6.2f}%   {r_t:7.3f} ms | {c_acc:6.2f}%   {c_t:7.3f} ms | {p_acc:6.2f}%   {p_t:7.3f} ms", flush=True)


def print_overall_summary(results):
    print_header("OVERALL BENCHMARK RESULTS SUMMARY")
    print(f"{'Dataset':<30} | {'Features':<8} | {'C++ Time':<10} | {'Python Time':<12} | {'Speedup':<10}", flush=True)
    print(f"{'-'*75}", flush=True)
    for r in results:
        print(f"{r['dataset']:<30} | {r['features']:<8} | {r['cpp_avg_ms']:7.2f} ms | {r['py_avg_ms']:9.2f} ms | {r['speedup']:7.2f}x", flush=True)
    print(f"{'='*75}\n", flush=True)
