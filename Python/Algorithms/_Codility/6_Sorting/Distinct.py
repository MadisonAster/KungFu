'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
import unittest
from datetime import datetime

def Distinct(A):
    return len(set(A))

class test_Distinct(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(Distinct(A), output)
    def test_1(self):
        A = [1]
        output = 1
        self.assertEqual(Distinct(A), output)
    def test_2(self):
        A = [1,2]
        output = 2
        self.assertEqual(Distinct(A), output)
    def test_3(self):
        A = [1,2,1]
        output = 2
        self.assertEqual(Distinct(A), output)
    def test_long(self):
        A = list(range(-100000,100000))
        output = 200000
        self.assertEqual(Distinct(A), output)

if __name__ == '__main__':
    unittest.main()