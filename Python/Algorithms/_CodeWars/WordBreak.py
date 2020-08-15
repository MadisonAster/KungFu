import unittest

def solution(s, wordDict):
    for word in wordDict:
        s = s.replace(word, '')
    return len(s) == 0

class MyTests(unittest.TestCase):
    def test_1(self):
        input0 = 'leetcode'
        input1 = ['leet', 'code']
        expected = True
        self.assertEqual(solution(input0, input1), expected)
    def test_2(self):
        input0 = 'cars'
        input1 = ['car', 'ca', 'rs']
        expected = True #They say this should be True, according to test_3 this would be False
        print(solution(input0, input1))
        self.assertEqual(solution(input0, input1), expected)
    def test_3(self):
        input0 = 'catsandog'
        input1 = ["cats", "dog", "sand", "and", "cat"]
        expected = False #They say this should be False, according to test_2 this would be True
        print(solution(input0, input1))
        self.assertEqual(solution(input0, input1), expected)

if __name__ == '__main__':
    unittest.main()