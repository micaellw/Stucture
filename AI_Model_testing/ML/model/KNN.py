#K-Nearest Neighbors
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier


def K_nn(X_train, X_test , y_train ,y_test):

    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy