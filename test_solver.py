from unittest import TestCase
from solver import Solver


class TestSolver(TestCase):

    def test_solve(self):

        s = Solver()
        result = s.solve()

        self.assertEquals(result, "test")
