'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
import unittest
from datetime import datetime

def TapeEquilibrium(A):
    CurrentBest = 9999
    beg = 0
    end = sum(A)
    for n in A[:-1]:
        beg += n
        end -= n
        diff = abs(beg-end)
        if diff < CurrentBest:
            CurrentBest = diff
    return CurrentBest

class test_TapeEquilibrium(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_small(self):
        A = [1,2]
        output = 1
        self.assertEqual(TapeEquilibrium(A), output)
    def test_example(self):
        A = [3,1,2,4,3]
        output = 1
        self.assertEqual(TapeEquilibrium(A), output)
    def test_extreme(self):
        A = [1000, -1000]
        output = 2000
        self.assertEqual(TapeEquilibrium(A), output)
    def test_extreme2(self):
        A = [1000, 3, 1000, -1000]
        output = 997
        self.assertEqual(TapeEquilibrium(A), output)
    def test_extreme3(self):
        A = list(range(10000))
        output = 3030
        self.assertEqual(TapeEquilibrium(A), output)

if __name__ == '__main__':
    unittest.main()