import unittest
from datetime import datetime

def BubbleSort(Array):
    for i in range(len(Array)-1):
        for j in range(0, len(Array[i:])-1):
            if Array[j] > Array[j+1] : 
                Array[j], Array[j+1] = Array[j+1], Array[j] 
    return Array

class test_BubbleSort(unittest.TestCase):
    def setUp(self):
        self.starttime = datetime.now()
    def tearDown(self):
        t = datetime.now() - self.starttime
        print(str(t), self.id())

    def test_1(self):
        Array = list(reversed(range(1000)))
        self.assertEqual(BubbleSort(Array), list(range(1000)))

if __name__ == '__main__':
    unittest.main()
