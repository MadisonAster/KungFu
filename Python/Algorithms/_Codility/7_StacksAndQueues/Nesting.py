'''
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
'''
import unittest
from datetime import datetime

def CodilityNesting(S):
    count = 0
    for a in S:
        if a == '(':
            count += 1
        elif count > 0 and a == ')':
            count -= 1
        else:
            return 0
    return int(count == 0)

class test_CodilityNesting(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        S = ''
        output = 1
        self.assertEqual(CodilityNesting(S), output)
    def test_0(self):
        S = '(()(())())'
        output = 1
        self.assertEqual(CodilityNesting(S), output)
    def test_1(self):
        S = ')))))((((('
        output = 0
        self.assertEqual(CodilityNesting(S), output)
    def test_2(self):
        S = '(()(())())('
        output = 0
        self.assertEqual(CodilityNesting(S), output)

if __name__ == '__main__':
    unittest.main()