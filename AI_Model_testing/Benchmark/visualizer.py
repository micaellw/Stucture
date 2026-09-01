# Benchmark/visualizer.py - High-Resolution In-Depth Graphical Visualization
# Visualizes PSO execution timings, speedup factor, classifier accuracy, and inference/training time

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set aesthetics
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8


def generate_all_plots(results, output_dir=None):
    """
    Generates and saves 3 comprehensive, high-resolution benchmark visualization files.
    """
    if output_dir is None:
        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    os.makedirs(output_dir, exist_ok=True)
    print(f"\n{'='*75}", flush=True)
    print(" GENERATING IN-DEPTH COMPARATIVE VISUALIZATIONS & PLOTS...", flush=True)
    print(f"{'='*75}", flush=True)

    dataset_names = [r["dataset"] for r in results]
    cpp_avgs = [r["cpp_avg_ms"] for r in results]
    py_avgs = [r["py_avg_ms"] for r in results]
    speedups = [r["speedup"] for r in results]
    model_names = ["Decision Tree", "Random Forest", "KNN", "SVM"]

    # =========================================================================
    # 1. PSO TIMING & SPEEDUP DASHBOARD (benchmark_timing_comparison.png)
    # =========================================================================
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    x = np.arange(len(dataset_names))
    width = 0.35

    # 1A: Execution Time (Log Scale)
    bars1 = axes[0].bar(x - width/2, cpp_avgs, width, label='C++ Engine (Multi-threaded)', color='#2b5c8f', edgecolor='black', alpha=0.9)
    bars2 = axes[0].bar(x + width/2, py_avgs, width, label='Pure Python Engine', color='#e76f51', edgecolor='black', alpha=0.9)

    axes[0].set_yscale('log')
    axes[0].set_ylabel('Execution Time (ms, Log Scale)', fontsize=12, fontweight='bold')
    axes[0].set_title('PSO Execution Time Comparison (C++ vs Pure Python)', fontsize=14, fontweight='bold', pad=12)
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(dataset_names, fontsize=11, fontweight='bold')
    axes[0].legend(fontsize=11)
    axes[0].grid(True, linestyle='--', alpha=0.6, which='both')

    for bar in bars1:
        yval = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2.0, yval * 1.15, f"{yval:.2f} ms", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1d3557')
    for bar in bars2:
        yval = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2.0, yval * 1.15, f"{yval:.2f} ms", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#9c3d25')

    # 1B: Speedup Factor
    bars_speed = axes[1].bar(dataset_names, speedups, color='#2a9d8f', edgecolor='black', width=0.45, alpha=0.9)
    axes[1].set_ylabel('Speedup Factor (X Times Faster)', fontsize=12, fontweight='bold')
    axes[1].set_title('Empirical Speedup: C++ over Pure Python', fontsize=14, fontweight='bold', pad=12)
    axes[1].set_xticks(range(len(dataset_names)))
    axes[1].set_xticklabels(dataset_names, fontsize=11, fontweight='bold')
    axes[1].grid(True, linestyle='--', alpha=0.6)

    for bar in bars_speed:
        yval = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2.0, yval + (max(speedups)*0.02), f"{yval:.1f}x Faster", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1b4332')

    plt.tight_layout()
    timing_plot_path = os.path.join(output_dir, "benchmark_timing_comparison.png")
    plt.savefig(timing_plot_path, dpi=300)
    plt.close()
    print(f"  [+] Saved Execution Time Chart : {timing_plot_path}", flush=True)

    # =========================================================================
    # 2. DOWNSTREAM MODEL PERFORMANCE: ACCURACY & EXECUTION TIME COMPARISON
    #    (benchmark_models_comparison.png)
    # =========================================================================
    n_datasets = len(results)
    fig, axes = plt.subplots(2, n_datasets, figsize=(6.5 * n_datasets, 10))

    if n_datasets == 1:
        axes = np.expand_dims(axes, axis=1)

    colors = ['#8d99ae', '#2b5c8f', '#e76f51'] # Raw, C++ PSO, Python PSO
    x_m = np.arange(len(model_names))
    w = 0.26

    for col_idx, r in enumerate(results):
        # Top Row: Model Accuracy (%)
        ax_acc = axes[0, col_idx]
        raw_accs = [r["models"]["Raw"][m]["accuracy"] for m in model_names]
        cpp_accs = [r["models"]["CPP"][m]["accuracy"] for m in model_names]
        py_accs = [r["models"]["Python"][m]["accuracy"] for m in model_names]

        ax_acc.bar(x_m - w, raw_accs, w, label='Without PSO (Full)', color=colors[0], edgecolor='black', alpha=0.85)
        b2 = ax_acc.bar(x_m, cpp_accs, w, label='C++ PSO Features', color=colors[1], edgecolor='black', alpha=0.9)
        ax_acc.bar(x_m + w, py_accs, w, label='Python PSO Features', color=colors[2], edgecolor='black', alpha=0.9)

        ax_acc.set_title(f"{r['dataset']}\n[Accuracy Comparison]", fontsize=12, fontweight='bold')
        ax_acc.set_xticks(x_m)
        ax_acc.set_xticklabels(model_names, fontsize=10, fontweight='bold', rotation=15)
        ax_acc.set_ylim(40, 105)
        ax_acc.set_ylabel('Model Accuracy (%)' if col_idx == 0 else '', fontsize=11, fontweight='bold')
        ax_acc.grid(True, linestyle='--', alpha=0.5)
        if col_idx == 0:
            ax_acc.legend(fontsize=9, loc='lower right')

        for b in b2:
            ax_acc.text(b.get_x() + b.get_width()/2, b.get_height() + 0.8, f"{b.get_height():.1f}%", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#1d3557')

        # Bottom Row: Model Execution / Inference Time (ms)
        ax_time = axes[1, col_idx]
        raw_times = [r["models"]["Raw"][m]["time_ms"] for m in model_names]
        cpp_times = [r["models"]["CPP"][m]["time_ms"] for m in model_names]
        py_times = [r["models"]["Python"][m]["time_ms"] for m in model_names]

        ax_time.bar(x_m - w, raw_times, w, label='Without PSO (Full)', color=colors[0], edgecolor='black', alpha=0.85)
        b_t2 = ax_time.bar(x_m, cpp_times, w, label='C++ PSO Features', color=colors[1], edgecolor='black', alpha=0.9)
        ax_time.bar(x_m + w, py_times, w, label='Python PSO Features', color=colors[2], edgecolor='black', alpha=0.9)

        ax_time.set_title(f"{r['dataset']}\n[Execution Time / Latency]", fontsize=12, fontweight='bold')
        ax_time.set_xticks(x_m)
        ax_time.set_xticklabels(model_names, fontsize=10, fontweight='bold', rotation=15)
        ax_time.set_ylabel('Model Train/Eval Time (ms)' if col_idx == 0 else '', fontsize=11, fontweight='bold')
        ax_time.grid(True, linestyle='--', alpha=0.5)
        if col_idx == 0:
            ax_time.legend(fontsize=9, loc='upper right')

        for b in b_t2:
            ax_time.text(b.get_x() + b.get_width()/2, b.get_height() + 0.1, f"{b.get_height():.2f}ms", ha='center', va='bottom', fontsize=8, fontweight='bold', color='#1d3557')

    plt.suptitle("Downstream Classifier Performance: Accuracy (%) & Execution Time (ms) Trade-off", fontsize=15, fontweight='bold', y=0.99)
    plt.tight_layout()
    models_plot_path = os.path.join(output_dir, "benchmark_models_comparison.png")
    plt.savefig(models_plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [+] Saved Model Performance & Time Chart: {models_plot_path}", flush=True)

    # =========================================================================
    # 3. FULL MASTER BENCHMARK DASHBOARD (benchmark_full_dashboard.png)
    # =========================================================================
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(2, 3, hspace=0.32, wspace=0.28)

    # Panel 1: Execution Time per Dataset (Log Scale)
    ax1 = fig.add_subplot(gs[0, 0])
    x_pos = np.arange(len(dataset_names))
    ax1.bar(x_pos - width/2, cpp_avgs, width, yerr=[r['cpp_std_ms'] for r in results], capsize=5, label='C++ PSO', color='#2b5c8f', edgecolor='black', alpha=0.9)
    ax1.bar(x_pos + width/2, py_avgs, width, yerr=[r['py_std_ms'] for r in results], capsize=5, label='Python PSO', color='#e76f51', edgecolor='black', alpha=0.9)
    ax1.set_yscale('log')
    ax1.set_ylabel('Execution Time (ms, Log Scale)', fontsize=11, fontweight='bold')
    ax1.set_title('1. PSO Execution Time (Log Scale)', fontsize=12, fontweight='bold')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(dataset_names, fontsize=9, fontweight='bold', rotation=10)
    ax1.legend(fontsize=9)
    ax1.grid(True, linestyle='--', alpha=0.6, which='both')

    # Panel 2: Speedup Factor
    ax2 = fig.add_subplot(gs[0, 1])
    bars_s = ax2.bar(dataset_names, speedups, color='#2a9d8f', edgecolor='black', width=0.45, alpha=0.9)
    ax2.set_ylabel('Speedup Factor (X)', fontsize=11, fontweight='bold')
    ax2.set_title('2. C++ Speedup Factor vs Python', fontsize=12, fontweight='bold')
    ax2.set_xticks(range(len(dataset_names)))
    ax2.set_xticklabels(dataset_names, fontsize=9, fontweight='bold', rotation=10)
    ax2.grid(True, linestyle='--', alpha=0.6)
    for bar in bars_s:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + (max(speedups)*0.02), f"{yval:.1f}x", ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Panel 3: Feature Dimension Reduction
    ax3 = fig.add_subplot(gs[0, 2])
    orig_feats = [r["features"] for r in results]
    cpp_feats = [r["cpp_selected_avg"] for r in results]
    py_feats = [r["py_selected_avg"] for r in results]

    ax3.bar(x_pos - width, orig_feats, width, label='Original Features', color='#8d99ae', edgecolor='black', alpha=0.7)
    ax3.bar(x_pos, cpp_feats, width, label='C++ Selected', color='#2b5c8f', edgecolor='black', alpha=0.9)
    ax3.bar(x_pos + width, py_feats, width, label='Python Selected', color='#e76f51', edgecolor='black', alpha=0.9)
    ax3.set_ylabel('Feature Count', fontsize=11, fontweight='bold')
    ax3.set_title('3. Feature Dimension Reduction', fontsize=12, fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(dataset_names, fontsize=9, fontweight='bold', rotation=10)
    ax3.legend(fontsize=9)
    ax3.grid(True, linestyle='--', alpha=0.6)

    # Panel 4: Overall Average Model Accuracy
    ax4 = fig.add_subplot(gs[1, 0])
    raw_acc_all = [np.mean([r["models"]["Raw"][m]["accuracy"] for m in model_names]) for r in results]
    cpp_acc_all = [np.mean([r["models"]["CPP"][m]["accuracy"] for m in model_names]) for r in results]
    py_acc_all = [np.mean([r["models"]["Python"][m]["accuracy"] for m in model_names]) for r in results]

    ax4.bar(x_pos - width, raw_acc_all, width, label='Without PSO (Full)', color='#8d99ae', edgecolor='black', alpha=0.7)
    ax4.bar(x_pos, cpp_acc_all, width, label='C++ PSO Features', color='#2b5c8f', edgecolor='black', alpha=0.9)
    ax4.bar(x_pos + width, py_acc_all, width, label='Python PSO Features', color='#e76f51', edgecolor='black', alpha=0.9)
    ax4.set_ylabel('Mean Model Accuracy (%)', fontsize=11, fontweight='bold')
    ax4.set_title('4. Mean Classifier Accuracy Across Models', fontsize=12, fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(dataset_names, fontsize=9, fontweight='bold', rotation=10)
    ax4.set_ylim(50, 100)
    ax4.legend(fontsize=9)
    ax4.grid(True, linestyle='--', alpha=0.6)

    # Panel 5: Overall Average Model Execution Time
    ax5 = fig.add_subplot(gs[1, 1])
    raw_time_all = [np.mean([r["models"]["Raw"][m]["time_ms"] for m in model_names]) for r in results]
    cpp_time_all = [np.mean([r["models"]["CPP"][m]["time_ms"] for m in model_names]) for r in results]
    py_time_all = [np.mean([r["models"]["Python"][m]["time_ms"] for m in model_names]) for r in results]

    ax5.bar(x_pos - width, raw_time_all, width, label='Without PSO (Full)', color='#8d99ae', edgecolor='black', alpha=0.7)
    ax5.bar(x_pos, cpp_time_all, width, label='C++ PSO Features', color='#2b5c8f', edgecolor='black', alpha=0.9)
    ax5.bar(x_pos + width, py_time_all, width, label='Python PSO Features', color='#e76f51', edgecolor='black', alpha=0.9)
    ax5.set_ylabel('Mean Model Time (ms)', fontsize=11, fontweight='bold')
    ax5.set_title('5. Mean Classifier Train/Inference Latency', fontsize=12, fontweight='bold')
    ax5.set_xticks(x_pos)
    ax5.set_xticklabels(dataset_names, fontsize=9, fontweight='bold', rotation=10)
    ax5.legend(fontsize=9)
    ax5.grid(True, linestyle='--', alpha=0.6)

    # Panel 6: Accuracy vs Time Scatter Trade-off
    ax6 = fig.add_subplot(gs[1, 2])
    for idx, r in enumerate(results):
        r_mean_acc = np.mean([r["models"]["Raw"][m]["accuracy"] for m in model_names])
        r_mean_time = np.mean([r["models"]["Raw"][m]["time_ms"] for m in model_names])
        c_mean_acc = np.mean([r["models"]["CPP"][m]["accuracy"] for m in model_names])
        c_mean_time = np.mean([r["models"]["CPP"][m]["time_ms"] for m in model_names])

        ax6.scatter(r_mean_time, r_mean_acc, color='#8d99ae', s=120, marker='o', label='Full Features' if idx == 0 else "")
        ax6.scatter(c_mean_time, c_mean_acc, color='#2b5c8f', s=140, marker='^', label='PSO Reduced' if idx == 0 else "")
        ax6.annotate(r["dataset"].split()[0], (c_mean_time, c_mean_acc), textcoords="offset points", xytext=(5, 5), fontsize=8, fontweight='bold')

    ax6.set_xlabel('Mean Model Latency (ms)', fontsize=11, fontweight='bold')
    ax6.set_ylabel('Mean Accuracy (%)', fontsize=11, fontweight='bold')
    ax6.set_title('6. Accuracy vs Latency Trade-off Space', fontsize=12, fontweight='bold')
    ax6.legend(fontsize=9)
    ax6.grid(True, linestyle='--', alpha=0.6)

    plt.suptitle("C++ vs Pure Python PSO Feature Selection — Comprehensive Benchmark & ML Model Dashboard", fontsize=16, fontweight='bold', y=0.98)
    dashboard_plot_path = os.path.join(output_dir, "benchmark_full_dashboard.png")
    plt.savefig(dashboard_plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [+] Saved Full Master Dashboard : {dashboard_plot_path}", flush=True)
    print(f"{'='*75}\n", flush=True)
