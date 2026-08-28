#ส่ง Dataset ไปส่วนต่างๆ
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from .Computational_Intelligence.CI_Model.PSO.BPSO.PSOmain import acceptData
from .model.DecisionTree import DecisionModel
from .model.Train_Test_Split import Train_Test 
from .model.Random_Forest import RF
from .model.KNN import K_nn
from .model.SVM import svm
from .model.prepare_data_universal import prepare_Data_universal
import time

class SendData:

    data = load_breast_cancer()
    
    X , y= prepare_Data_universal(sklearn_dataset=data)

    execution_time = 0

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_selected , best_mask , FitnessSore ,timepso = acceptData(X_scaled , y)

    X_trainPso, X_testPso , y_trainPso ,y_testPso = Train_Test(X_selected,y)
    X_train, X_test , y_train ,y_test = Train_Test(X,y)

    
    def DicisionTree_PSO(self):

        if self.X_selected.shape[1] == 0:
            return 0
    
        start_time = time.perf_counter()
        self.score = DecisionModel( self.X_trainPso, self.X_testPso , self.y_trainPso ,self.y_testPso )
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time
       
        return self.score 
    
    def DicisionTree(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = DecisionModel( self.X_train, self.X_test , self.y_train ,self.y_test )
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 
    
    def Random_Forest_PSO(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = RF(self.X_trainPso, self.X_testPso , self.y_trainPso ,self.y_testPso)
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 
    
    def Random_Forest(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = RF(self.X_train, self.X_test , self.y_train ,self.y_test )
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 
    
    def KNN_PSO(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = K_nn(self.X_trainPso, self.X_testPso , self.y_trainPso ,self.y_testPso)
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time
        
        return self.score 
    
    def KNN(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = K_nn(self.X_train, self.X_test , self.y_train ,self.y_test )
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 
    
    def SVM_PSO(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = svm(self.X_trainPso, self.X_testPso , self.y_trainPso ,self.y_testPso)
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 
    
    def SVM(self):

        if self.X_selected.shape[1] == 0:
            return 0
        
        start_time = time.perf_counter()
        self.score = svm(self.X_train, self.X_test , self.y_train ,self.y_test )
        end_time = time.perf_counter()

        self.execution_time = end_time - start_time

        return self.score 


