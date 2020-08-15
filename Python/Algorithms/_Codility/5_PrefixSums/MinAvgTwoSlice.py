'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''
import unittest
from datetime import datetime
import math

def MinAvgTwoSlice(A):
    minaverage = (A[0] + A[1])/2.0  
    minavg_index = 0     
    for index in range(0, len(A)-2):
        if (A[index] + A[index+1]) / 2.0 < minaverage:
            minaverage = (A[index] + A[index+1]) / 2.0
            minavg_index = index
        if (A[index] + A[index+1] + A[index+2]) / 3.0 < minaverage:
            minaverage = (A[index] + A[index+1] + A[index+2]) / 3.0
            minavg_index = index
    if (A[-1]+A[-2])/2.0 < minaverage:
        minaverage = (A[-1]+A[-2])/2.0
        minavg_index = len(A)-2
    return minavg_index

class test_MinAvgTwoSlice(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_Example(self):
        A = [4,2,2,5,1,5,8]
        output = 1
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_1(self):
        A = [10000,-10000,4000,0,10000,10000,10000]
        output = 1
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_2(self):
        A = [3,3,1,2,3,4,5,6,7,8,9,10]
        output = 2
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_3(self):
        A = [10000,10000,-10000,9000,-8000,7000,-6000,5000,-4000,3000,-2000,1000,0]
        output = 2
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_4(self):
        A = [10000,-10000,10000,-8000,-5000]
        output = 3
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_5(self):
        A = [10000,-10000,10000,-8000,-5000]
        output = 3
        self.assertEqual(MinAvgTwoSlice(A), output)
    def test_long(self):
        A = []
        count = -10000
        for i in range(0,100000):
            if count > 0:
                count *= -1
                A.append(count)
            elif count < 0:
                count *= -1
                count -= 1
                A.append(count)
            elif count == 0:
                A.append(count)
                break
        output = 1
        self.assertEqual(MinAvgTwoSlice(A), output)

if __name__ == '__main__':
    unittest.main()

