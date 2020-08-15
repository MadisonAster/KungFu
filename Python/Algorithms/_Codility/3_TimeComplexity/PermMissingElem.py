'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
import unittest
from datetime import datetime

def PermMissingElem(A):
    if len(A) == 0:
        return 1
    elif len(A) == max(A):
        return max(A)+1
    else:
        return list(set(range(1,max(A))) - set(A))[0]

class test_PermMissingElem(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 1
        self.assertEqual(PermMissingElem(A), output)
    def test_single(self):
        A = [2]
        output = 1
        self.assertEqual(PermMissingElem(A), output)
    def test_double(self):
        A = [2,3]
        output = 1
        self.assertEqual(PermMissingElem(A), output)
    def test_1(self):
        A = [2,3,1,5]
        output = 4
        self.assertEqual(PermMissingElem(A), output)
    def test_2(self):
        A = [2,3,1,4]
        output = 5
        self.assertEqual(PermMissingElem(A), output)
    def test_long(self):
        A = list(range(1,100001))
        A.remove(42)
        output = 42
        self.assertEqual(PermMissingElem(A), output)

if __name__ == '__main__':
    unittest.main()