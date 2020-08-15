'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000]
'''
import unittest
from datetime import datetime

def PermCheck(A):
    if len(A) != 0:
        if len(A) == len(set(A)):
            A.sort()
            if len(A) == A[-1]:
                return 1
    return 0


class test_PermCheck(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(PermCheck(A), output)
    def test_single(self):
        A = [1]
        output = 1
        self.assertEqual(PermCheck(A), output)
    def test_double(self):
        A = [2,3]
        output = 0
        self.assertEqual(PermCheck(A), output)
    def test_single(self):
        A = [2]
        output = 0
        self.assertEqual(PermCheck(A), output)
    def test_example(self):
        A = [4,1,3,2]
        output = 1
        self.assertEqual(PermCheck(A), output)
    def test_example2(self):
        A = [4,1,3]
        output = 0
        self.assertEqual(PermCheck(A), output)
    def test_weird(self):
        A = [1]*10 + [11]
        output = 0
        self.assertEqual(PermCheck(A), output)
    def test_dup(self):
        A = [1,1,2,3,4]
        output = 0
        self.assertEqual(PermCheck(A), output)
 
if __name__ == '__main__':
    unittest.main()