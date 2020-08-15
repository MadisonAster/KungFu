'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''
import unittest
from datetime import datetime

def CodilityTriangle(A):
    A.sort()
    return int(bool([True for i in range(len(A[:-2])) if A[i]+A[i+1]>A[i+2]]))

class test_CodilityTriangle(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_single(self):
        A = [1]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_double(self):
        A = [1,1]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_equilateral(self):
        A = [1,1,1]
        output = 1
        self.assertEqual(CodilityTriangle(A), output)
    def test_equilateralN(self):
        A = [-1,-1,-1]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_000(self):
        A = [0,0,0]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_neg(self):
        A = [-10,-10,-10]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_1(self):
        A = [10,2,5,1,8,20]
        output = 1
        self.assertEqual(CodilityTriangle(A), output)
    def test_1a(self):
        A = [-10,-2,-5,-1,-8,-20]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_1c(self):
        A = [-10,-2,-5,-1,-8,-20,10,2,5,1,8,20]
        output = 1
        self.assertEqual(CodilityTriangle(A), output)
    def test_2(self):
        A = [10,50,5,3]
        output = 0
        self.assertEqual(CodilityTriangle(A), output)
    def test_long(self):
        A = list(range(1,1000))
        output = 1
        self.assertEqual(CodilityTriangle(A), output)
    def test_long2(self):
        A = list(range(1,100000))
        output = 1
        self.assertEqual(CodilityTriangle(A), output)
    def test_long3(self):
        A = list(range(-100000,100000))
        output = 1
        self.assertEqual(CodilityTriangle(A), output)

if __name__ == '__main__':
    unittest.main()