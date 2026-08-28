// Fitness.cpp การคำนวน fitness
#include "Fitness.hpp"
#include <cmath>

using namespace std;

double evaluate_binary(
    const vector<int>& mask,
    const vector<vector<double>>& X,
    const vector<int>& y 
) {
    int rows = X.size();
    int cols = X[0].size();
    int selected = 0;

    for (int m : mask)
        if (m == 1) selected++;

    if (selected == 0) return -1e9;

    double total_fisher_score = 0.0;

    for (int j = 0; j < cols; j++) {
        if (mask[j] == 0) continue;

        double sum0 = 0.0, sum1 = 0.0;
        int count0 = 0, count1 = 0;

        for (int i = 0; i < rows; i++) {
            if (y[i] == 0) { sum0 += X[i][j]; count0++; }
            else { sum1 += X[i][j]; count1++; }
        }

        double mean0 = (count0 > 0) ? sum0 / count0 : 0.0;
        double mean1 = (count1 > 0) ? sum1 / count1 : 0.0;

        double var0 = 0.0, var1 = 0.0;

        for (int i = 0; i < rows; i++) {
            if (y[i] == 0) var0 += (X[i][j] - mean0) * (X[i][j] - mean0);
            else var1 += (X[i][j] - mean1) * (X[i][j] - mean1);
        }

        var0 = (count0 > 0) ? var0 / count0 : 0.0;
        var1 = (count1 > 0) ? var1 / count1 : 0.0;

        double denominator = var0 + var1;
        double fisher = 0.0;
        if (denominator > 1e-9) { 
            fisher = ((mean0 - mean1) * (mean0 - mean1)) / denominator;
        }

        total_fisher_score += fisher;
    }

    double avg_fisher = total_fisher_score / selected;
    double feature_ratio = (double)selected / cols;

    return avg_fisher - (0.05 * feature_ratio);
}


double evaluate_multiclass(const vector<int>& mask, const vector<vector<double>>& X, const vector<int>& y, int num_classes) {
    int rows = X.size();
    int cols = X[0].size();
    int selected = 0;

    for (int m : mask) if (m == 1) selected++;
    if (selected == 0) return -1e9;

    double total_score = 0.0;

    for (int j = 0; j < cols; j++) {
        if (mask[j] == 0) continue;

        double global_mean = 0.0;
        for (int i = 0; i < rows; i++) global_mean += X[i][j];
        global_mean /= rows;

        double between_class_scatter = 0.0; // ความห่างระหว่างคลาส
        double within_class_scatter = 0.0;  // ความเกาะกลุ่มในคลาส

        // คำนวณทีละคลาส (0 ถึง num_classes-1)
        for (int c = 0; c < num_classes; c++) {
            double class_mean = 0.0;
            double class_var = 0.0;
            int count = 0;

            for (int i = 0; i < rows; i++) {
                if (y[i] == c) {
                    class_mean += X[i][j];
                    count++;
                }
            }
            if (count == 0) continue;
            class_mean /= count;

            for (int i = 0; i < rows; i++) {
                if (y[i] == c) {
                    double diff = X[i][j] - class_mean;
                    class_var += diff * diff;
                }
            }
            
            between_class_scatter += count * pow(class_mean - global_mean, 2);
            within_class_scatter += class_var;
        }

        double fisher = (within_class_scatter > 0) ? (between_class_scatter / within_class_scatter) : 0;
        total_score += fisher;
    }

    double avg_score = total_score / selected;
    double penalty = 0.05 * ((double)selected / cols);
    
    return avg_score - penalty;
}