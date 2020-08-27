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
        Array[len(Array)-1] = -5
        self.assertEqual(LinearSearch(Array, -5), len(Array)-1)
        Array[500] = -5
        self.assertEqual(LinearSearch(Array, -5), 500)
        
    def test_2(self):
        Array = list(range(10000))
        random.shuffle(Array)
        Array[len(Array)-1] = -5
        self.assertEqual(LinearSearch(Array, -5), len(Array)-1)
        Array[500] = -5
        self.assertEqual(LinearSearch(Array, -5), 500)

if __name__ == '__main__':
    unittest.main()
