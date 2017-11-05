import sys
import HelperMethods as hm

class Solution:

    def solve(self, in_file_stream, out=sys.stdout):
        sample_read = hm.readVal(int, in_file_stream)
        hm.write_line(out, "Solve me!")

#########################################
# Solution().solve(sys.stdin, sys.stdout)