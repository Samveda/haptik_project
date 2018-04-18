import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import  metrics
classifier = RandomForestClassifier(n_estimators=200)


def q07_roc_auc_score(X_train_dtm,X_test_dtm,y_train,y_test):
    "write your solution here"
    classifier.fit(X_train_dtm, y_train.astype(int))
    y_pred = classifier.predict(X_test_dtm)
    a = np.array(y_test.values.astype(int))
    overall_accuracy = metrics.roc_auc_score(y_test.astype(int).values, y_pred)
    print(overall_accuracy)
    label_accuracy = np.sum(np.array(y_pred == a)) / (y_pred.shape[0] * y_pred.shape[1])
    print(label_accuracy)
    return overall_accuracy, label_accuracy
