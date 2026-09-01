# index.py - Show Feature Selection, Model Performance, and C++ vs Python Timing Comparison
from ML.main import SendData

# 1. Initialize C++ Engine (Default)
Data_cpp = SendData(engine="cpp")

# 2. Initialize Pure Python Engine (Same Formula & Logic)
Data_py = SendData(engine="python")

print('\n================= FEATURE =================\n')
print(f'Total Features : {len(Data_cpp.X[1])}')

print('\n========== PSO FEATURE SELECTION (C++ vs PYTHON) ==========\n')

print('--- C++ PSO Engine ---')
print(f'Selected Features count : {len(Data_cpp.X_selected[1])}')
print(f'Selected BEST Features  : {Data_cpp.best_mask}')
print(f'FITNESS SCORE           : {Data_cpp.FitnessSore:.6f}')
print(f'TIME OF CALCULATED PSO  : {Data_cpp.timepso:.6f} seconds ({Data_cpp.timepso*1000:.3f} ms)\n')

print('--- Pure Python PSO Engine ---')
print(f'Selected Features count : {len(Data_py.X_selected[1])}')
print(f'Selected BEST Features  : {Data_py.best_mask}')
print(f'FITNESS SCORE           : {Data_py.FitnessSore:.6f}')
print(f'TIME OF CALCULATED PSO  : {Data_py.timepso:.6f} seconds ({Data_py.timepso*1000:.3f} ms)\n')

speedup = Data_py.timepso / Data_cpp.timepso if Data_cpp.timepso > 0 else 0
print(f'>>> SPEEDUP PROOF: C++ is {speedup:.2f}x FASTER than Python on the exact same algorithm! <<<\n')

print('\n============ MODEL PERFORMANCE (Using C++ PSO Features) ============\n')

print('MODEL WITHOUT PSO :\n')
print(f'Decision Tree Accuracy : {Data_cpp.DicisionTree()}')
print(f'TIME OF Decision Tree  : {Data_cpp.execution_time:.6f} seconds\n')

print(f'Random Forest Accuracy : {Data_cpp.Random_Forest()}')
print(f'TIME OF Random Forest  : {Data_cpp.execution_time:.6f} seconds\n')

print(f'KNN Accuracy           : {Data_cpp.KNN()}')
print(f'TIME OF KNN            : {Data_cpp.execution_time:.6f} seconds\n')

print(f'SVM Accuracy           : {Data_cpp.SVM()}')
print(f'TIME OF SVM            : {Data_cpp.execution_time:.6f} seconds\n')


print('\nMODEL WITH PSO :\n')
print(f'Decision Tree Accuracy : {Data_cpp.DicisionTree_PSO()}')
print(f'TIME OF Decision Tree  : {Data_cpp.execution_time:.6f} seconds\n')

print(f'Random Forest Accuracy : {Data_cpp.Random_Forest_PSO()}')
print(f'TIME OF Random Forest  : {Data_cpp.execution_time:.6f} seconds\n')

print(f'KNN Accuracy           : {Data_cpp.KNN_PSO()}')
print(f'TIME OF KNN            : {Data_cpp.execution_time:.6f} seconds\n')

print(f'SVM Accuracy           : {Data_cpp.SVM_PSO()}')
print(f'TIME OF SVM            : {Data_cpp.execution_time:.6f} seconds\n')
