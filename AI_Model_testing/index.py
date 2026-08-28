#index.py       Show A Comparison
from ML.main import SendData

Data = SendData()
print('\n================= FEATURE =================\n')

print(f'Total Features : {len(Data.X[1])}')



print('\n========== PSO FEATURE SELECTION ==========\n')

print(f'Selected Features : {len(Data.X_selected[1])}')
print(f'Selected BEST Features : {Data.best_mask}')
print(f'FITNESS SCORE : {Data.FitnessSore}')
print(f'TIME OF CALCULATED PSO : {Data.timepso:.6f} seconds')



print('\n============ MODEL PERFORMANCE ============\n')

print('MODEL WITHOUT PSO :\n')
print(f'Decision Tree Accuracy : {Data.DicisionTree()}')
print(f'TIME OF Decision Tree : {Data.execution_time:.6f} seconds\n')

print(f'Random Forest Accuracy : {Data.Random_Forest()}')
print(f'TIME OF Random Forest : {Data.execution_time:.6f} seconds\n')

print(f'KNN Accuracy : {Data.KNN()}')
print(f'TIME OF KNN : {Data.execution_time:.6f} seconds\n')

print(f'SVM Accuracy : {Data.SVM()}')
print(f'TIME OF SVM : {Data.execution_time:.6f} seconds\n')


print('\nMODEL WITH PSO :\n')
print(f'Decision Tree Accuracy : {Data.DicisionTree_PSO()}')
print(f'TIME OF Decision Tree : {Data.execution_time:.6f} seconds\n')

print(f'Random Forest Accuracy : {Data.Random_Forest_PSO()}')
print(f'TIME OF Random Forest : {Data.execution_time:.6f} seconds\n')

print(f'KNN Accuracy : {Data.KNN_PSO()}')
print(f'TIME OF KNN : {Data.execution_time:.6f} seconds\n')

print(f'SVM Accuracy  : {Data.SVM_PSO()}')
print(f'TIME OF SVM : {Data.execution_time:.6f} seconds\n')
