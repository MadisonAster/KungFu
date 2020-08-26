'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

'''
import unittest
from datetime import datetime

def MaxDoubleSliceSum(N):
    if len(N) <= 3:
        return 0

    return 0

class test_MaxDoubleSliceSum(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_single(self):
        A = [10]
        output = 10
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_example(self):
        A = [3, 2, -6, 4, 0]
        output = 5
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_1(self):
        A = [3, 2, -6, 4, 2]
        output = 6
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_2(self):
        A = [3, 2, -4, 4, 2]
        output = 7
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_3(self):
        A = [3, 2, -10000, 10000,-10000,10000,-10000, 4, 2]
        output = 10000
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_4(self):
        A = [4000, 4000, 4000, -10000, 10000,-10000, 5000, 5000, 5000, -10000, -10000]
        output = 17000
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_5(self):
        A = [-20,-10,-1000,-1000,-1000,-15]
        output = -10
        self.assertEqual(MaxDoubleSliceSum(A), output)
    def test_long(self):
        A = [1] * 1000000
        output = 1000000
        self.assertEqual(MaxDoubleSliceSum(A), output)

if __name__ == '__main__':
    unittest.main()
'''