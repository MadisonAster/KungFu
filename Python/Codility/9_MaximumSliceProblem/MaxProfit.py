'''
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
'''
import unittest
from datetime import datetime

def solution1(A):
    if len(A) < 2:
        return 0
    maxprofit = 0
    for i, n in enumerate(A[:-1]):
        p = max(A[i+1:])-n
        if p > maxprofit:
            maxprofit = p
    return maxprofit


def solution2(A):
    if len(A) < 2:
        return 0
    if len(A) < 5000:
        return solution1(A)
    maxprice = max(A[1:])
    minprice = min(A[:-1])
    maxindex = len(A)-1-list(reversed(A)).index(maxprice)
    minindex = A.index(minprice)
    p1 = max(A[minindex+1:])-minprice
    p2 = maxprice-min(A[:maxindex]) 
    return max(0,p1,p2)

def solution(A):
    if len(A) < 2:
        return 0
    maxprice = max(A[1:])
    minprice = min(A[:-1])
    maxindex = len(A)-1-list(reversed(A)).index(maxprice)
    minindex = A.index(minprice)
    p1 = max(A[minindex+1:])-minprice
    p2 = maxprice-min(A[:maxindex]) 
    if minindex > maxindex:
        p3 = solution(A[maxindex:minindex])
    else:
        p3 = 0
    return max(0,p1,p2,p3)



class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        input = []
        output = 0
        self.assertEqual(solution(input), output)
    def test_single(self):
        input = [1]
        output = 0
        self.assertEqual(solution(input), output)
    def test_double1(self):
        input = [1,2]
        output = 1
        self.assertEqual(solution(input), output)
    def test_double2(self):
        input = [2,1]
        output = 0
        self.assertEqual(solution(input), output)


    def test_example(self):
        input = [23171,21011,21123,21366,21013,21367]
        output = 356
        self.assertEqual(solution(input), output)

    def test_example2(self):
        input = [100,100,100,100,900,9000,10,1,10000]
        output = 9999
        self.assertEqual(solution(input), output)


    def test_chaos(self):
        input = [100,1000,0,1000,100,-100,100,100,100]
        output = 1000
        self.assertEqual(solution(input), output)


    def test_chaos2(self):
        input = [999,1000,100,500,999,1,100]
        output = 899
        self.assertEqual(solution(input), output)

    def test_long(self):
        input0 = []
        count = 100000
        for i in range(0,count):
            input0.append(i)
        input0.append(100100)
        output = 100100
        self.assertEqual(solution(input0), output)

if __name__ == '__main__':
    unittest.main()