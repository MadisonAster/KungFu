import unittest
import random
from datetime import datetime

def LinearSearch(Array, n):
    for i, m in enumerate(Array):
        if m == n:
            return i
    else:
        return -1

class test_LinearSearch(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(reversed(range(10000)))
        self.assertEqual(LinearSearch(Array, 50), 949)

    def test_2(self):
        Array = list(range(10000))
        random.shuffle(Array)
        Array[500] = 1000
        self.assertEqual(LinearSearch(Array, 1000), 500)

if __name__ == '__main__':
    unittest.main()
