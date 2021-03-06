'''
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
'''

'''
import TestKit
from datetime import datetime

def NumberOfDiscIntersections(N):
    return 0

class test_NumberOfDiscIntersections(TestKit.TimedTest):

    def test_0(self):
        N = 0
        output = 0
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_1(self):
        N = 1
        output = 1
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_17(self):
        N = 17
        output = 2
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_9(self):
        N = 9
        output = 3
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_24(self):
        N = 24
        output = 8
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long1(self):
        N = 1000000000
        output = 100
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long2(self):
        N = 10000000000
        output = 121
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long3(self):
        N = 2147483646
        output = 192
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long4(self):
        N = 2147483648
        output = 32
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long5(self):
        N = 2147483647
        output = 2
        self.assertEqual(NumberOfDiscIntersections(N), output)
    def test_long6(self):
        N = 780291637
        output = 2
        self.assertEqual(NumberOfDiscIntersections(N), output)

if __name__ == '__main__':
    unittest.main()
'''