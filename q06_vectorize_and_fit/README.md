# Vectorize_and_fit


## Write a function `q06_vectorize_and_fit` that 
- Use CountVectorizer along with parameters ngram_range=(1, 2), analyzer=lambda doc:doc,tokenizer = TreebankWordTokenizer.tokenize  
- And do fit_transorm to train and transform to test dataset
  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| X_train | dataframe | compulsory |  | dataframe to be trained  |
| X_test | dataframe | compulsory |  | dataframe to be trained  |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| X_train_dtm | dataframe | clean data frame |
| X_test_dtm | dataframe | clean data frame |

