import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import TreebankWordTokenizer


def q06_vectorize_and_fit(X_train, X_test):
    "write your solution here"
    vect = CountVectorizer(ngram_range=(1, 2), analyzer=lambda doc:doc,tokenizer = TreebankWordTokenizer.tokenize)
    X_train_dtm = vect.fit_transform(X_train)
    X_test_dtm = vect.transform(X_test)
    return X_train_dtm, X_test_dtm