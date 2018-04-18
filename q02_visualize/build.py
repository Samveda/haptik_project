import pandas as pd
import os, sys
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_load_data_and_split.build import q01_load_data_and_split

path = 'data/train_data.csv'

def q02_visualize(path):
    "write your solution here"
    data, X_train, y_train = q01_load_data_and_split(path, encoding='UTF-8')
    name = list(y_train.columns.values)
    counts = []
    for i in name:
        counts.append(data[i].sum())
    df = pd.DataFrame(sorted(counts))
    df = df.T
    df.columns = name
    df.plot(kind = 'bar', figsize=(7,7))
    plt.xlabel('categories')
    plt.ylabel('values')
    plt.title('Distribution values class-wise')
    plt.show()    


print(q02_visualize(path))