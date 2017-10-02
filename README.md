# Kattis Solution

Python 3 scaffolding for solving Kattis problems.

# Solving

Solutions should go in Solution.py file.

# Setup

Run init.ps1 [POBLEM_NAME] script to setup the project.

# Unit tests

For unit tests to work all output needs to be written to _out_

    def solve(self, in_file_stream, out=sys.stdout):
      out.write('expected output')

# Submitting

Be sure to uncomment this line: 

    Solution().solve(sys.stdin, sys.stdout)
    
Replace _out_ calls with _print_.
