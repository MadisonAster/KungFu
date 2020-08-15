'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
import unittest
from datetime import datetime

import math

def MaxProductOfThree(A):
    if len(A) < 3:
        return None

    a = sorted(A)

    p1 = a[0]*a[1]*a[-1]
    p2 = a[-1]*a[-2]*a[-3]
    return max(p1,p2)

class test_MaxProductOfThree(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_one(self):
        A = [5,4,3,2,1,0,-5]
        output = 60
        self.assertEqual(MaxProductOfThree(A), output)
    def test_two(self):
        A = [5,4,3,2,1,0,-5,-5]
        output = 125
        self.assertEqual(MaxProductOfThree(A), output)
    def test_three(self):
        A = [5,5,1,2,1,0,-5,-5]
        output = 125
        self.assertEqual(MaxProductOfThree(A), output)
    def test_four(self):
        A = [5,5,1,2,1,0,-4,-5]
        output = 100
        self.assertEqual(MaxProductOfThree(A), output)

if __name__ == '__main__':
    unittest.main()