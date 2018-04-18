import os, sys
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from q01_load_data_and_split.build import q01_load_data_and_split
from q04_preprocessing.build import q04_preprocessing
import pandas as pd
from ..build import q06_vectorize_and_fit
from unittest import TestCase
from inspect import getfullargspec


path = 'data/train_data.csv'
path1 = 'data/test_data.csv'

remove =  [u'ok',u'don',u'yeah',u'hai',u'thank',u'hey',u'dear',u'use',u'let know',u'near',u'pl',u'ur',u'ya',u'kya',
           u'sure',u'go',u'train',u'plz',u'much',u'give',u'good',u'plea',u'like',u'ye',u'know',u'u',u'se','okay',
           u'nd',u'pls',u'ac',u'app',u'est',u'stop',u'hi',u'rs',u'ok',u'list',u'hello',u'dont',u'yet',u'take',
           u'also',u'done',u'make',u'going',u'ye',u'hii',u'got',u'menu',u'day',u'll',u'ye',u'still',u'ley',u'gb',
           u'hi want',u'want ook',u'ka',u'wan na',u'haptik',u'wake call',u'much',u'g',u'will',u'didn',u'please']

data_train, X_train, y_train = q01_load_data_and_split(path, encoding='UTF-8')
data_test, X_test, y_test = q01_load_data_and_split(path1, encoding='UTF-8')
X_train_processed = pd.Series(q04_preprocessing(X_train,rm_words=remove))
X_test_processed = pd.Series(q04_preprocessing(X_test,rm_words=remove))


X_train_dtm, X_test_dtm = q06_vectorize_and_fit(X_train_processed, X_test_processed)

class TestPlotResiduals(TestCase):
    def test_arguements(self):

        # Input parameters tests
        args = getfullargspec(q06_vectorize_and_fit)
        self.assertEqual(len(args[0]), 2, "Expected argument(s) %d, Given %d" % (2 ,len(args[0])))

    def test_defaults(self):
        args = getfullargspec(q06_vectorize_and_fit)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    def test_shape_train(self):
        self.assertEqual(X_train_dtm.shape, (40659,15405),"Return value shape does not match expected value")

    def test_shape_test(self):
        self.assertEqual(X_test_dtm.shape, (10000,15405),"Return value shape does not match expected value")