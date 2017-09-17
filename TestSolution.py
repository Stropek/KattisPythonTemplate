from io import StringIO
from unittest import TestCase
from nose_parameterized import parameterized
from FilesFinder import *
from Solution import *

def get_test_case_sources():
    parameters = []
    test_files = FilesFinder().find_test_files()

    for test_file in test_files:
        parameters.append((test_file, test_file.replace(".in", ".ans")))
    return parameters


class TestSolution(TestCase):

    @parameterized.expand(get_test_case_sources())
    def test_solve(self, in_file, ans_file):
        out_stream = StringIO()

        in_file_stream = open("TestFiles/" + in_file, "r")
        ans_file_stream = open("TestFiles/" + ans_file, "r")

        Solution().solve(in_file_stream, out=out_stream)

        out_file_stream = out_stream.getvalue()

        for out_line in out_file_stream.split('\n'):
            ans_line = ans_file_stream.readline()
            self.assertEqual(ans_line.strip('\n'), out_line)
