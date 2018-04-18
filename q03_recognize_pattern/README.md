# Recognize_pattern

In this task, you need recognize the pattern which not relevant examples like date, phone numbers etc..

We will replace them with some text so that when we are creating a model it understand.

These pattern are first recognize via regex statements, so we will using three regex statements
- `'[0-9]{1,2} ?(am|pm)'` this will replaced by timeofday
- `'[0-9]{1,2} ?(hours?|hrs?|mins?|minutes?)'` replaced by durationtext
- `'[0-9]{10}\D'` replaced by phonenumber

## Write a function `q03_recognize_pattern` that 
- Uses re modules to replace as shown above. 
- Try to understand how re function are used

[re module](https://docs.python.org/3/library/re.html) 

  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| corpus | dataframe | compulsory |  | dataframe from which we need to remove non character  |


### Returns:


| Return | dtype | description |
| --- | --- | --- | 
| corpus | dataframe | clean data frame |

