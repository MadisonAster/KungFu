import unittest
from datetime import datetime

def FindPath(nums, target):
    ibuffer = []
    def recurse_find(nums, ibuffer=None):
        for i, a in enumerate(nums):
            ibuffer.append(i)
            if type(a) == list:
                for b in recurse_find(a, ibuffer=ibuffer):
                    yield b
            else:
                yield a
            ibuffer.pop(-1)
    for val in recurse_find(nums, ibuffer=ibuffer):
        if val == target:
            return ibuffer
class test_FindPath(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        nums = [0, 42, [300, [], 200, [[101]]], 1000, 200]
        expected = [2, 3, 0, 0]
        self.assertEqual(FindPath(nums, 101), expected)

        target = nums
        for i in expected:
            target = target[i]
        self.assertEqual(target, 101)

if __name__ == '__main__':
    unittest.main()
