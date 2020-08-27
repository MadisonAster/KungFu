'''
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
'''


import unittest
from datetime import datetime
import math

def CodilityFlags(A):
    if len(A) < 3:
        return 0

    peaks = []
    for i, n in enumerate(A):
        if i == 0 or i == len(A)-1:
            continue
        if n > A[i-1] and n > A[i+1]:
            peaks.append(i)
    count = len(peaks)
    lastcounted = -math.inf
    for i in peaks:
        if i-lastcounted < count:
            count -= 1
        else:
            lastcounted = i
    return count

class test_CodilityFlags(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        A = []
        output = 0
        self.assertEqual(CodilityFlags(A), output)
    def test_1(self):
        A = [5]
        output = 0
        self.assertEqual(CodilityFlags(A), output)
    def test_2(self):
        A = [0,5]
        output = 0
        self.assertEqual(CodilityFlags(A), output)
    def test_3(self):
        A = [0,5,1]
        output = 1
        self.assertEqual(CodilityFlags(A), output)
    def test_4(self):
        A = [2,0,1]
        output = 0
        self.assertEqual(CodilityFlags(A), output)
    def test_5(self):
        A = [1,5,3,4,3,4,1,2,3,4,6,2]
        output = 3
        self.assertEqual(CodilityFlags(A), output)



if __name__ == '__main__':
    unittest.main()
