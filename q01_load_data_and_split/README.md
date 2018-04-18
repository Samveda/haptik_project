# Load data 

Your job is to read the files present in data given.

## Write a function `q01_load_data_and_split` that 
- read the data from the data folder and use encoding='UTF-8' while reading the file.
- splits into X_train and y_train and return dataframe, X_train and y_train

  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| path | String | compulsory |  | Path of data folder |
| encoding | str | optional | 'UTF-8' | character encoding |



### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| dataframe | dataframe | text belonging to each category of data |
| X_train | dataframe | training data set |
| y_train | pandas.Series |training target variable|
