'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
import unittest
from datetime import datetime

def solution(A):
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]
    A.sort()
    for i, n in enumerate(A):
        if i+1 == len(A):
            return n
        if i % 2 == 0:
            if n != A[i+1]:
                return n

class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())
    
    def test_empty(self):
        A = []
        output = None
        self.assertEqual(solution(A), output)
    def test_single(self):
        A = [1]
        output = 1
        self.assertEqual(solution(A), output)

    def test_example(self):
        A = [9,3,9,3,9,7,9]
        output = 7
        self.assertEqual(solution(A), output)
    def test_end(self):
        A = [5,5,3,4,4]
        output = 3
        self.assertEqual(solution(A), output)
    def test_long(self):
        A = []
        count = 1000000
        for i in range(0,count):
            A.append(i)
            A.append(i)
        A.append(10001)
        output = 10001
        self.assertEqual(solution(A), output)

if __name__ == '__main__':
    unittest.main()