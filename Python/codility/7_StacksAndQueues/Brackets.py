'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''
import unittest
from datetime import datetime

def solution(S):
    bstack = []
    match = {
    '{' : '}',
    '[' : ']',
    '(' : ')',
    }
    for a in S:
        if a in ['(','[','{']:
            bstack.append(match[a])
        elif len(bstack) > 0 and a == bstack[-1]:
            bstack.pop()
        else:
            return 0
    return int(len(bstack) == 0)

class test_solution(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_empty(self):
        S = ''
        output = 1
        self.assertEqual(solution(S), output)
    def test_0(self):
        S = '(()(())())'
        output = 1
        self.assertEqual(solution(S), output)
    def test_1(self):
        S = ')))))((((('
        output = 0
        self.assertEqual(solution(S), output)
    def test_2(self):
        S = '(()(())())('
        output = 0
        self.assertEqual(solution(S), output)
    def test_3(self):
        S = '{[()()]}'
        output = 1
        self.assertEqual(solution(S), output)
    def test_4(self):
        S = '([)()]'
        output = 0
        self.assertEqual(solution(S), output)

if __name__ == '__main__':
    unittest.main()