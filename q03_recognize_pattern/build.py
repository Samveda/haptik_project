import pandas as pd
import re
import string


def q03_recognize_pattern(corpus):
    "write your solution here"

    '''
    Adds useful features to improve the model
    '''

    # TimeofDay
    corpus = [re.sub('[0-9]{1,2} ?(am|pm)', 'timeofday', text) for text in corpus]

    # Minutes/hour
    corpus = [re.sub('[0-9]{1,2} ?(hours?|hrs?|mins?|minutes?)', 'durationtext', text) for text in corpus]

    # Phone number or pnr
    corpus = [re.sub('[0-9]{10}\D', 'phonenumber', text) for text in corpus]
    return corpus
