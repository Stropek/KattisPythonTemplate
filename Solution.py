import sys

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        sample_read = readVal(int, in_file_stream)
        write_line(out, "Solve me!")


def readVal(parse, in_stream):
    return parse(in_stream.readline().strip("\n").split(' '))
def readValsMap(parse, in_stream):
    return map(parse, in_stream.readline().strip("\n").split(' '))
def readValsList(parse, in_stream): 
    return list(map(parse, in_stream.readline().strip("\n").split(' ')))
def readInt(in_stream):
    return readVal(int, in_stream)
def readIntsMap(in_stream):
    return readValsMap(int, in_stream)
def readIntsList(in_stream):
    return readValsList(int, in_stream)

def write_line(out, text):
    if out == sys.stdout:
        print(str(text) + "\n")
    else: 
        out.write(str(text) + "\n")

#########################################
# Solution().solve(sys.stdin, sys.stdout)