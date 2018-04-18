from unittest import TestCase
from ..build import q02_visualize
from unittest import TestCase
from inspect import getfullargspec


class TestPlotResiduals(TestCase):
    def test_plot_residuals_arguements(self):

        # Input parameters tests
        args = getfullargspec(q02_visualize)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args[0])))

    def test_plot_residuals_defaults(self):
        args = getfullargspec(q02_visualize)
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")