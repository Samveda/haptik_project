import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_load_data_and_split
from inspect import getfullargspec
import pandas


path = 'data/train_data.csv'
df, X, y = q01_load_data_and_split(path, encoding='UTF-8')


class TestRead_csv_data_to_df(TestCase):
    def test_read_csv_data_to_df_args(self):
        arg = getfullargspec(q01_load_data_and_split).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (2, len(arg)))

    def test_load_data_defaults(self):
        args = getfullargspec(q01_load_data_and_split)
        self.assertEqual(args[3], ('UTF-8',), "Expected default values do not match given default values")

    def test_read_csv_data_to_df_return_instance(self):
        self.assertIsInstance(df, pandas.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(df.shape, (40659, 10), "The Expected return shape does not match with the given return shape")

