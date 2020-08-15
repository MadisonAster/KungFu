'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
'''
import unittest
from datetime import datetime

def MaxSliceSum(A):
    if len(A) == 0:
        return 0
    best = -2147483648
    current = -2147483648
    for i in A:
        current = current + i
        current = max(current, -2147483648)
        current = max(current, i)
        best = max(best, current)
    return best

class test_MaxSliceSum(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(MaxSliceSum(A), output)
    def test_single(self):
        A = [10]
        output = 10
        self.assertEqual(MaxSliceSum(A), output)
    def test_example(self):
        A = [3, 2, -6, 4, 0]
        output = 5
        self.assertEqual(MaxSliceSum(A), output)
    def test_1(self):
        A = [3, 2, -6, 4, 2]
        output = 6
        self.assertEqual(MaxSliceSum(A), output)
    def test_2(self):
        A = [3, 2, -4, 4, 2]
        output = 7
        self.assertEqual(MaxSliceSum(A), output)
    def test_3(self):
        A = [3, 2, -10000, 10000,-10000,10000,-10000, 4, 2]
        output = 10000
        self.assertEqual(MaxSliceSum(A), output)
    def test_4(self):
        A = [4000, 4000, 4000, -10000, 10000,-10000, 5000, 5000, 5000, -10000, -10000]
        output = 17000
        self.assertEqual(MaxSliceSum(A), output)
    def test_5(self):
        A = [-20,-10,-1000,-1000,-1000,-15]
        output = -10
        self.assertEqual(MaxSliceSum(A), output)
    def test_long(self):
        A = [1] * 1000000
        output = 1000000
        self.assertEqual(MaxSliceSum(A), output)

if __name__ == '__main__':
    unittest.main()