import unittest
import random
from datetime import datetime

def InsertionSort(Array):
    for i in range(1, len(Array)): 
        key = Array[i]

        j = i-1
        while j >= 0 and key < Array[j] : 
                Array[j + 1] = Array[j] 
                j -= 1
        Array[j + 1] = key
    return Array

class test_InsertionSort(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(reversed(range(1000)))
        self.assertEqual(InsertionSort(Array), list(range(1000)))

    def test_2(self):
        Array = list(range(1000))
        random.shuffle(Array)
        self.assertEqual(InsertionSort(Array), list(range(1000)))

if __name__ == '__main__':
    unittest.main()
