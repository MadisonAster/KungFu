import unittest
import random
from datetime import datetime

def BinarySearch(Array, n, low=0, high=None):
    if high == None:
        high = len(Array)-1
    if high >= low:
        mid = low + (high - low) // 2
        if Array[mid] == n:
            return mid
        elif Array[mid] > n:
            return BinarySearch(Array, n, low=low, high=mid-1)
        else:
            return BinarySearch(Array, n, low=mid+1, high=high)
    else:
        return -1

class test_BinarySearch(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(range(100000))
        self.assertEqual(BinarySearch(Array, Array[-1]), len(Array)-1)

    def test_std(self):
        Array = list(range(100000))
        self.assertEqual(Array.index(Array[-1]), len(Array)-1)


if __name__ == '__main__':
    unittest.main()
