'''
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

class Solution { public int solution(int X, int Y, int D); }

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
'''
import unittest
from datetime import datetime
import math

def FrogJmp(X, Y, D):
    return math.ceil((Y-X)/D)

class test_FrogJmp(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        X = 10
        Y = 85
        D = 30
        output = 3
        self.assertEqual(FrogJmp(X,Y,D), output)
    def test_long(self):
        X = 0
        Y = 1000000000
        D = 1
        output = 1000000000
        self.assertEqual(FrogJmp(X,Y,D), output)

if __name__ == '__main__':
    unittest.main()