'''
Write a function:

class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''
import unittest
from datetime import datetime
import math

def solution(A,B,K):
    count = 0
    if A % K == 0:
        count += 1
    elif B % K == 0:
        count += 1
    elif (A % K) > (B % K):
        count += 1
    count += math.floor((B-A)/K)
    return count

class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_MM(self):
        A,B,K = 6, 15, 3
        output = 4
        self.assertEqual(solution(A, B, K), output)
    def test_ML(self):
        A,B,K = 6, 14, 3
        output = 3
        self.assertEqual(solution(A, B, K), output)
    def test_MG(self):
        A,B,K = 6, 16, 3
        output = 4
        self.assertEqual(solution(A, B, K), output)
    def test_LM(self):
        A,B,K = 5, 15, 3
        output = 4
        self.assertEqual(solution(A, B, K), output)
    def test_LL(self):
        A,B,K = 5, 14, 3
        output = 3
        self.assertEqual(solution(A, B, K), output)
    def test_LG(self):
        A,B,K = 5, 16, 3
        output = 4
        self.assertEqual(solution(A, B, K), output)
    def test_GM(self):
        A,B,K = 7, 15, 3
        output = 3
        self.assertEqual(solution(A, B, K), output)
    def test_GL(self):
        A,B,K = 7, 14, 3
        output = 2
        self.assertEqual(solution(A, B, K), output)
    def test_GG(self):
        A,B,K = 7, 16, 3
        output = 3
        self.assertEqual(solution(A, B, K), output)
    def test_0M(self):
        A,B,K = 0, 15, 3
        output = 6
        self.assertEqual(solution(A, B, K), output)
    def test_0L(self):
        A,B,K = 0, 14, 3
        output = 5
        self.assertEqual(solution(A, B, K), output)
    def test_0G(self):
        A,B,K = 0, 16, 3
        output = 6
        self.assertEqual(solution(A, B, K), output)
    def test_FA(self):
        A,B,K = 11, 345, 17
        output = 20
        self.assertEqual(solution(A, B, K), output)

if __name__ == '__main__':
    unittest.main()