'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''
import unittest
from datetime import datetime

import math

def CodilityDominator(A):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return 0
    a = sorted(A)
    i = math.floor(len(a)/2)
    D = a[i]
    if A.count(D) > len(A)/2:
        return A.index(D)
    return -1



class test_CodilityDominator(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_one(self):
        input0 = [2,1,2,1,1]
        output = 1
        self.assertEqual(CodilityDominator(input0), output)
    def test_two(self):
        input0 = [2,1,2,1,2]
        output = 0
        self.assertEqual(CodilityDominator(input0), output)
    def test_three(self):
        input0 = [2,1,2,1,2,3,3,3,3,3]
        output = -1
        self.assertEqual(CodilityDominator(input0), output)
    def test_four(self):
        input0 = []
        output = -1
        self.assertEqual(CodilityDominator(input0), output)
    def test_five(self):
        input0 = [0]
        output = 0
        self.assertEqual(CodilityDominator(input0), output)

if __name__ == '__main__':
    unittest.main()