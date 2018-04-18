from unittest import TestCase
from ..build import q03_recognize_pattern
from unittest import TestCase
from inspect import getfullargspec


class TestPlotResiduals(TestCase):
    def test_plot_residuals_arguements(self):

        # Input parameters tests
        args = getfullargspec(q03_recognize_pattern)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))
