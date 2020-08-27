import unittest
import random
from datetime import datetime

def SelectionSort(Array):
    for i in range(len(Array)):
        j = Array.index(min(Array[i:]))
        Array[i], Array[j] = Array[j], Array[i]
    return Array

class test_SelectionSort(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(reversed(range(1000)))
        self.assertEqual(SelectionSort(Array), list(range(1000)))

    def test_2(self):
        Array = list(range(1000))
        random.shuffle(Array)
        self.assertEqual(SelectionSort(Array), list(range(1000)))


if __name__ == '__main__':
    unittest.main()
