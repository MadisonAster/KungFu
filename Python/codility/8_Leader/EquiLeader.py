'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''
import unittest
from datetime import datetime

def solution(N):
    return 0

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
        output = 1
        self.assertEqual(solution(N), output)
    def test_17(self):
        N = 17
        output = 2
        self.assertEqual(solution(N), output)
    def test_9(self):
        N = 9
        output = 3
        self.assertEqual(solution(N), output)
    def test_24(self):
        N = 24
        output = 8
        self.assertEqual(solution(N), output)
    def test_long1(self):
        N = 1000000000
        output = 100
        self.assertEqual(solution(N), output)
    def test_long2(self):
        N = 10000000000
        output = 121
        self.assertEqual(solution(N), output)
    def test_long3(self):
        N = 2147483646
        output = 192
        self.assertEqual(solution(N), output)
    def test_long4(self):
        N = 2147483648
        output = 32
        self.assertEqual(solution(N), output)
    def test_long5(self):
        N = 2147483647
        output = 2
        self.assertEqual(solution(N), output)
    def test_long6(self):
        N = 780291637
        output = 2
        self.assertEqual(solution(N), output)

if __name__ == '__main__':
    unittest.main()