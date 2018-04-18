# Preprocessing


## Write a function `q04_preprocessing` that 

In this task, we need to use the previous function and need to perform following task. 

1. Remove all punctuation
2. Removes text in between curly braces (internal haptik data)
3. Remove all stopwords and custom defined words
4. Performs stemming
5. Returns a list of the cleaned text

  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| corpus | dataframe | compulsory |  | dataframe from which we need to remove non character  |
| punc | Boolean | optional | True | Punctuation is present |
| stem | Boolean | optional | True | p_stemmer is present |
| rm_words | list | optional | [] | add more words to stop words |

### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| corpus | dataframe | clean data frame |

