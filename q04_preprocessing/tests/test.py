from unittest import TestCase
from ..build import q04_preprocessing
from unittest import TestCase
from inspect import getfullargspec


class TestPlotResiduals(TestCase):
    def test_arguements(self):

        # Input parameters tests
        args = getfullargspec(q04_preprocessing)
        self.assertEqual(len(args[0]), 4, "Expected argument(s) %d, Given %d" % (4, len(args[0])))

    def test_defaults(self):
        args = getfullargspec(q04_preprocessing)
        self.assertEqual(args[3], (True, True, [],), "Expected default values do not match given default values")
