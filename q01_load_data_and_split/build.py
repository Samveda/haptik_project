import pandas as pd
import numpy as np



def q01_load_data_and_split(path, encoding='UTF-8'):
    "write your solution here"
    dataframe = pd.read_csv(path, encoding=encoding )
    X_train = dataframe.iloc[:,0]
    y_train = dataframe.iloc[:,1:]
    y_train.replace({'F':0, 'T':1},inplace=True)
    return dataframe,X_train, y_train

