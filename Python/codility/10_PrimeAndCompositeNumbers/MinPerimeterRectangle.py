'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

class Solution { public int solution(int N); }

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
'''
import unittest
from datetime import datetime
import math

def solution(N):
    if N == 0:
        A, B = 0, 0
    elif N == 1:
        A, B = 1, 1
    else:
        A = math.floor(math.sqrt(N))
        while N % A != 0:
            A -= 1
        B = N/A
    return int(2*(A+B))

class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_0(self):
        N = 0
        output = 0
        self.assertEqual(solution(N), output)
    def test_1(self):
        N = 1
        output = 4
        self.assertEqual(solution(N), output)
    def test_17(self):
        N = 17
        output = 36
        self.assertEqual(solution(N), output)
    def test_30(self):
        N = 30
        output = 22
        self.assertEqual(solution(N), output)
    def test_long(self):
        N = 1000000000
        output = 126500
        self.assertEqual(solution(N), output)

if __name__ == '__main__':
    unittest.main()