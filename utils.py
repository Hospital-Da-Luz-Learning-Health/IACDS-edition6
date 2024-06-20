import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

def measure_metrics(model, X, y):
    y_pred = model.predict(X)
    f1 = f1_score(y, y_pred)
    recall = recall_score(y, y_pred)
    precision = precision_score(y, y_pred)
    return {'f1_score':f1, 'recall':recall, 'precision':precision}

def display_metrics(clf, X_train, y_train, X_test, y_test):

    train_metrics = measure_metrics(clf,X_train,y_train)
    test_metrics = measure_metrics(clf,X_test,y_test)

    metrics_data = pd.DataFrame([train_metrics,test_metrics],index=['Train metrics', 'Test metrics'])

    return metrics_data