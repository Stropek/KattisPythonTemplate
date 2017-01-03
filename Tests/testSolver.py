from unittest import TestCase
from nose_parameterized import parameterized
from StringIO import StringIO
from solver import Solver
import os
from TestHelpers.filesFinder import FilesFinder


def getTestCaseSources():
    parameters = []
    testFiles = FilesFinder().findTestFiles()

    for testFile in testFiles:
        parameters.append((testFile, testFile.replace(".in", ".ans")))
    return parameters

class TestSolver(TestCase):

    @parameterized.expand(getTestCaseSources())
    def test_solve(self, inFile, ansFile):
        outStream = StringIO()

        inFileStream = open("../TestFiles/" + inFile, "rb")
        ansFileStream = open("../TestFiles/" + ansFile, "rb")

        Solver().solve(inFileStream, out=outStream)

        outFileStream = outStream.getvalue()

        for outLine in outFileStream.split('\n'):
            ansLine = ansFileStream.readline()
            self.assertEquals(ansLine.strip('\n'), outLine)
