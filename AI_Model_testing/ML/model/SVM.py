#Support Vector Machine
from sklearn.metrics import accuracy_score 
from sklearn.svm import SVC

def svm(X_train, X_test , y_train ,y_test):

    clf = SVC(kernel="linear")

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy