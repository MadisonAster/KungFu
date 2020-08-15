'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
'''
import unittest
from datetime import datetime

def MaxCounters(N, A):
    result = [0] * N
    highest = 0
    for o in set(A):
        if o <= N:
            break
    else:
        return result
    for o in A:
        if o > N:
            result = [highest] * N
        else:
            result[o-1] += 1
            if result[o-1] > highest:
                highest = result[o-1]
    return result

class test_MaxCounters(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        N = 5
        A = []
        output = [0,0,0,0,0]
        self.assertEqual(MaxCounters(N, A), output)
    def test_empty2(self):
        N = 0
        A = []
        output = []
        self.assertEqual(MaxCounters(N, A), output)
    def test_single(self):
        N = 1
        A = [1]
        output = [1]
        self.assertEqual(MaxCounters(N, A), output)
    def test_single2(self):
        N = 1
        A = [2,2,2,2]
        output = [0]
        self.assertEqual(MaxCounters(N, A), output)
    def test_example(self):
        N = 5
        A = [3,4,4,6,1,4,4]
        output = [3,2,2,4,2]
        self.assertEqual(MaxCounters(N, A), output)
    def test_large(self):
        N = 5
        A = [2] * 10000 + [6] * 10000
        output = [10000,10000,10000,10000,10000]
        self.assertEqual(MaxCounters(N, A), output)
    def test_large(self):
        N = 5
        A = [6] * 10000000
        output = [0,0,0,0,0]
        self.assertEqual(MaxCounters(N, A), output)
    
if __name__ == '__main__':
    unittest.main()
