# train_test_split
from sklearn.model_selection import train_test_split


def Train_Test(X_selected , y):
    X_train, X_test, y_train, y_test = train_test_split(
        X_selected, y, test_size=0.3, random_state=42
    )

    
    return  X_train, X_test, y_train, y_test
