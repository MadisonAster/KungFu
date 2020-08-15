'''
This is a demo task.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
import unittest
from datetime import datetime

def MissingInteger(A):
    if len(A) != 0:
        A.append(0)
        A = list(set(A))
        A.sort()
        z = A.index(0)
        for i, n in enumerate(A[z:]):
            if n != i:
                return i
        else:
            return i+1
    return 1


class test_MissingInteger(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 1
        self.assertEqual(MissingInteger(A), output)
    def test_single(self):
        A = [1]
        output = 2
        self.assertEqual(MissingInteger(A), output)
    def test_double(self):
        A = [-2,-3,-4,2,3]
        output = 1
        self.assertEqual(MissingInteger(A), output)
    def test_example(self):
        A = [-1,-2,4,1,3,2]
        output = 5
        self.assertEqual(MissingInteger(A), output)
    def test_example2(self):
        A = [4,1,3]
        output = 2
        self.assertEqual(MissingInteger(A), output)
    def test_weird(self):
        A = [1]*10000 + [11]
        output = 2
        self.assertEqual(MissingInteger(A), output)
    def test_dup(self):
        A = [1,1,2,3,4]
        output = 5
        self.assertEqual(MissingInteger(A), output)
    def test_example3(self):
        A = [1,3,6,4,1,2]
        output = 5
        self.assertEqual(MissingInteger(A), output)
    
if __name__ == '__main__':
    unittest.main()
