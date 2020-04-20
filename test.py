# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from Bisection import Bisection
from Newtons import Newtons
from Secant import Secant
from Generalroots import RootStatus

class TestBisectionClass(unittest.TestCase):

    def setup(self):
        self.bisection = Bisection(lambda x: x**3 -x -1)

    def test_initialization(self):
        self.assertEqual(self.bisection.max_iter, None, 'incorrect max_iter')
        self.assertEqual(self.bisection.xn, [], 'incorrect xn intialization')
        self.assertEqual(self.bisection.status, RootStatus.pending, 'incorrect status')
        self.assertEqual(self.bisection.function_string, 'f(x) = x**3 -x -1', 'incorrect function string')

    def test_find_root_success(self):


    def test_find_root_max_iter(self):


    def test_find_root_fail(self):