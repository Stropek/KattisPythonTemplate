import sys

def readVal(parse, in_stream):
    return parse(in_stream.readline().strip("\n").split(' ')[0])
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

def write(out, text):
    if out == sys.stdout:
        print(str(text))
    else: 
        out.write(str(text))

def write_line(out, text):
    if out == sys.stdout:
        print(str(text) + "\n")
    else: 
        out.write(str(text) + "\n")