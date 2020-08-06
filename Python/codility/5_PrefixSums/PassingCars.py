'''
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''
import unittest
from datetime import datetime

def solution(A):
    count = 0
    zcount = 0
    z = 0
    for i, n in enumerate(A):
        if n == 1:
            zcount += A[z:i].count(0)
            z = i
            count += zcount
            if count > 1000000000:
                return -1
    return count

class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(solution(A), output)
    def test_single(self):
        A = [1]
        output = 0
        self.assertEqual(solution(A), output)
    def test_1(self):
        A = [0,1,0,1,1]
        output = 5
        self.assertEqual(solution(A), output)
    def test_long(self):
        A = [0,1] * 100000000
        output = -1
        self.assertEqual(solution(A), output)
    def test_long2(self):
        A = [0] * 10000000
        A.append(1)
        output = 10000000
        self.assertEqual(solution(A), output)
    def test_long3(self):
        A = [0] * 10000000
        A.insert(0, 1)
        A.append(1)
        A.append(1)
        output = 20000000
        self.assertEqual(solution(A), output)

if __name__ == '__main__':
    unittest.main()