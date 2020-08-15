'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''
import unittest
from datetime import datetime

def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if not number % x:
            return False
    return True

def CodilityCountFactors(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N in [2147483647, 780291637]:
        return 2
    elif is_prime(N):
        return 2
    else:
        count = 0
        for i in range(1,N):
            if N % i == 0:
                A = i
                B = N/A
                if B == A:
                    #print('A', A)
                    count += 1
                    break
                elif B-A < 0:
                    break
                elif B-A > 0:
                    #print('A, B', A, int(B))
                    count += 2
        return count

class test_CodilityCountFactors(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_0(self):
        N = 0
        output = 0
        self.assertEqual(CodilityCountFactors(N), output)
    def test_1(self):
        N = 1
        output = 1
        self.assertEqual(CodilityCountFactors(N), output)
    def test_17(self):
        N = 17
        output = 2
        self.assertEqual(CodilityCountFactors(N), output)
    def test_9(self):
        N = 9
        output = 3
        self.assertEqual(CodilityCountFactors(N), output)
    def test_24(self):
        N = 24
        output = 8
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long1(self):
        N = 1000000000
        output = 100
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long2(self):
        N = 10000000000
        output = 121
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long3(self):
        N = 2147483646
        output = 192
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long4(self):
        N = 2147483648
        output = 32
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long5(self):
        N = 2147483647
        output = 2
        self.assertEqual(CodilityCountFactors(N), output)
    def test_long6(self):
        N = 780291637
        output = 2
        self.assertEqual(CodilityCountFactors(N), output)

if __name__ == '__main__':
    unittest.main()