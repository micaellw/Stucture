# Fitness.py - Python equivalent of Fitness.cpp
# Contains fitness evaluation functions for Binary and Multiclass Classification

def evaluate_binary(mask, X, y):
    """
    Exact 1:1 translation of C++ evaluate_binary in Fitness.cpp
    Formula: Fisher score = (mean0 - mean1)^2 / (var0 + var1)
    Penalty: 0.05 * (selected_features / total_features)
    """
    rows = len(X)
    cols = len(X[0])
    selected = sum(1 for m in mask if m == 1)

    if selected == 0:
        return -1e9

    total_fisher_score = 0.0

    for j in range(cols):
        if mask[j] == 0:
            continue

        sum0 = 0.0
        sum1 = 0.0
        count0 = 0
        count1 = 0

        for i in range(rows):
            if y[i] == 0:
                sum0 += X[i][j]
                count0 += 1
            else:
                sum1 += X[i][j]
                count1 += 1

        mean0 = (sum0 / count0) if count0 > 0 else 0.0
        mean1 = (sum1 / count1) if count1 > 0 else 0.0

        var0 = 0.0
        var1 = 0.0

        for i in range(rows):
            if y[i] == 0:
                var0 += (X[i][j] - mean0) ** 2
            else:
                var1 += (X[i][j] - mean1) ** 2

        var0 = (var0 / count0) if count0 > 0 else 0.0
        var1 = (var1 / count1) if count1 > 0 else 0.0

        denominator = var0 + var1
        fisher = 0.0
        if denominator > 1e-9:
            fisher = ((mean0 - mean1) ** 2) / denominator

        total_fisher_score += fisher

    avg_fisher = total_fisher_score / selected
    feature_ratio = float(selected) / float(cols)

    return avg_fisher - (0.05 * feature_ratio)


def evaluate_multiclass(mask, X, y, num_classes):
    """
    Exact 1:1 translation of C++ evaluate_multiclass in Fitness.cpp
    Formula: Fisher score = between_class_scatter / within_class_scatter
    Penalty: 0.05 * (selected_features / total_features)
    """
    rows = len(X)
    cols = len(X[0])
    selected = sum(1 for m in mask if m == 1)

    if selected == 0:
        return -1e9

    total_score = 0.0

    for j in range(cols):
        if mask[j] == 0:
            continue

        global_mean = sum(X[i][j] for i in range(rows)) / rows

        between_class_scatter = 0.0
        within_class_scatter = 0.0

        # Calculate per class (0 to num_classes-1)
        for c in range(num_classes):
            class_mean = 0.0
            class_var = 0.0
            count = 0

            for i in range(rows):
                if y[i] == c:
                    class_mean += X[i][j]
                    count += 1

            if count == 0:
                continue

            class_mean /= count

            for i in range(rows):
                if y[i] == c:
                    diff = X[i][j] - class_mean
                    class_var += diff * diff

            between_class_scatter += count * ((class_mean - global_mean) ** 2)
            within_class_scatter += class_var

        fisher = (between_class_scatter / within_class_scatter) if within_class_scatter > 0 else 0.0
        total_score += fisher

    avg_score = total_score / selected
    penalty = 0.05 * (float(selected) / float(cols))

    return avg_score - penalty
